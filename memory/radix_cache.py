import time
from typing import Dict, List, Optional, Any

class RadixNode:
  def __init__(self, key: List[int], value: Any = None):
    self.key: List[int] = key
    self.value: Any = value
    self.children: Dict[int, 'RadixNode'] = None
    self.ref_count: int = 0
    
  def update_access_time(self):
    self.last_access_time = time.time()

class RadixCache:
  def __init__(self, capacity_blocks: int):
    self.root = RadixNode(key=[])
    self.capacity_blocks = capacity_blocks
    self.current_blocks = 0
    
  def match_prefix(self, tokens: List[int]):
    node = self.root
    matched_len = 0
    
    while matched_len < len(tokens):
      target_token = tokens[matched_len]
      if target_token not in node.children:
        break
        
      child = node.children[target_token]
      child_key_len = len(child.key)
      
      match_in_edge = 0
            while (match_in_edge < child_key_len and 
                   matched_len + match_in_edge < len(tokens) and
                   child.key[match_in_edge] == tokens[matched_len + match_in_edge]):
                match_in_edge += 1
            
            if match_in_edge == child_key_len:
                node = child
                matched_len += child_key_len
                node.update_access_time()
            else:
                matched_len += match_in_edge
                break
                
        return matched_len, node

    def insert(self, tokens: List[int], value: Any = None):
        node = self.root
        matched_len = 0
        
        while matched_len < len(tokens):
            target_token = tokens[matched_len]
            
            if target_token not in node.children:
                new_node = RadixNode(key=tokens[matched_len:], value=value)
                new_node.parent = node
                node.children[target_token] = new_node
                self.current_blocks += len(new_node.key)
                self.evict_lru()
                return
                
            child = node.children[target_token]
            child_key_len = len(child.key)
            
            match_in_edge = 0
            while (match_in_edge < child_key_len and 
                   matched_len + match_in_edge < len(tokens) and
                   child.key[match_in_edge] == tokens[matched_len + match_in_edge]):
                match_in_edge += 1
            
            if match_in_edge == child_key_len:
                node = child
                matched_len += child_key_len
                node.update_access_time()
            else:
                split_node = RadixNode(key=child.key[:match_in_edge])
                split_node.parent = node
                node.children[target_token] = split_node
                
                child.key = child.key[match_in_edge:]
                child.parent = split_node
                split_node.children[child.key[0]] = child
                
                remaining_tokens = tokens[matched_len + match_in_edge:]
                if remaining_tokens:
                    new_leaf = RadixNode(key=remaining_tokens, value=value)
                    new_leaf.parent = split_node
                    split_node.children[remaining_tokens[0]] = new_leaf
                    self.current_blocks += len(new_leaf.key)
                else:
                    split_node.value = value
                
                self.evict_lru()
                return

    def evict_lru(self):
        while self.current_blocks > self.capacity_blocks:
            evictable = []
            
            def collect_evictable(node):
                if node != self.root and node.ref_count == 0 and not node.children:
                    evictable.append(node)
                for child in node.children.values():
                    collect_evictable(child)
                    
            collect_evictable(self.root)
            
            if not evictable:
                break
                
            evictable.sort(key=lambda n: n.last_access_time)
            victim = evictable[0]
            
            self.current_blocks -= len(victim.key)
            parent = victim.parent
            del parent.children[victim.key[0]]
            
            if parent != self.root and len(parent.children) == 1 and parent.value is None and parent.ref_count == 0:
                only_child = list(parent.children.values())[0]
                parent.key.extend(only_child.key)
                parent.value = only_child.value
                parent.children = only_child.children
                for child in parent.children.values():
                    child.parent = parent

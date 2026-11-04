import time
from typing import List, Dict, Tuple, Optional

class TrieNode:
    def __init__(self, token: Optional[int] = None):
        self.token = token
        self.children: Dict[int, 'TrieNode'] = {}
        self.is_terminal: bool = False
        self.last_accessed: float = 0.0
        self.kv_cache_id: Optional[str] = None

class PrefixCacheTrie:
    def __init__(self, max_nodes: int = 1000):
        self.root = TrieNode()
        self.max_nodes = max_nodes
        self.node_count = 0

    def _update_access_time(self, node: TrieNode) -> None:
        node.last_accessed = time.time()

    def insert(self, tokens: List[int], kv_cache_id: str) -> None:
        curr = self.root
        self._update_access_time(curr)
        
        for token in tokens:
            if token not in curr.children:
                if self.node_count >= self.max_nodes:
                    self.evict_lru()
                curr.children[token] = TrieNode(token)
                self.node_count += 1
            curr = curr.children[token]
            self._update_access_time(curr)
            
        curr.is_terminal = True
        curr.kv_cache_id = kv_cache_id

    def match_longest_prefix(self, tokens: List[int]) -> Tuple[List[int], Optional[str]]:
        curr = self.root
        self._update_access_time(curr)
        
        current_match = []
        valid_matched_tokens = []
        best_kv_id = None
        
        for token in tokens:
            if token in curr.children:
                curr = curr.children[token]
                self._update_access_time(curr)
                current_match.append(token)
                
                if curr.is_terminal:
                    valid_matched_tokens = list(current_match)
                    best_kv_id = curr.kv_cache_id
            else:
                break
                
        return valid_matched_tokens, best_kv_id

    def evict_lru(self) -> None:
        oldest_time = float('inf')
        lru_leaf = None
        
        def _find_lru(node: TrieNode):
            nonlocal oldest_time, lru_leaf
            if node.is_terminal and node.last_accessed < oldest_time:
                oldest_time = node.last_accessed
                lru_leaf = node
            for child in node.children.values():
                _find_lru(child)
                
        _find_lru(self.root)
        
        if lru_leaf:
            lru_leaf.is_terminal = False
            lru_leaf.kv_cache_id = None

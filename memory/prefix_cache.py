from typing import Dict, List, Optional, Tuple


class TrieNode:
    def __init__(self, token: Optional[int] = None, parent: Optional["TrieNode"] = None):
        self.token = token
        self.parent = parent
        self.children: Dict[int, "TrieNode"] = {}
        self.is_terminal: bool = False
        self.last_accessed: int = 0
        self.kv_cache_id: Optional[str] = None


class PrefixCacheTrie:
    def __init__(self, max_nodes: int = 1000):
        self.root = TrieNode()
        self.max_nodes = max_nodes
        self.node_count = 0
        self._clock = 0

    def _touch(self, node: TrieNode) -> None:
        self._clock += 1
        node.last_accessed = self._clock

    def insert(self, tokens: List[int], kv_cache_id: str) -> None:
        curr = self.root
        self._touch(curr)
        for token in tokens:
            if token not in curr.children:
                curr.children[token] = TrieNode(token, parent=curr)
                self.node_count += 1
            curr = curr.children[token]
            self._touch(curr)
        curr.is_terminal = True
        curr.kv_cache_id = kv_cache_id

        while self.node_count > self.max_nodes:
            if not self.evict_lru():
                break

    def match_longest_prefix(self, tokens: List[int]) -> Tuple[List[int], Optional[str]]:
        curr = self.root
        self._touch(curr)
        current_match: List[int] = []
        valid_matched_tokens: List[int] = []
        best_kv_id = None
        for token in tokens:
            if token not in curr.children:
                break
            curr = curr.children[token]
            self._touch(curr)
            current_match.append(token)
            if curr.is_terminal:
                valid_matched_tokens = list(current_match)
                best_kv_id = curr.kv_cache_id
        return valid_matched_tokens, best_kv_id

    def evict_lru(self) -> bool:
        lru, stack = None, [self.root]
        while stack:
            node = stack.pop()
            if node.is_terminal and (lru is None or node.last_accessed < lru.last_accessed):
                lru = node
            stack.extend(node.children.values())
        if lru is None:
            return False

        lru.is_terminal = False
        lru.kv_cache_id = None
        node = lru
        while node is not self.root and not node.is_terminal and not node.children:
            del node.parent.children[node.token]
            self.node_count -= 1
            node = node.parent
        return True
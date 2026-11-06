import pytest
import time
from memory.radix_cache import RadixCache

def test_basic_insert_and_match():
    cache = RadixCache(capacity_blocks=100)
    
    cache.insert(tokens=[1, 2, 3, 4], value="prompt_1")
    
    match_len, node = cache.match_prefix([1, 2, 3, 4, 5, 6])
    assert match_len == 4
    assert node.value == "prompt_1"
    
    match_len, _ = cache.match_prefix([9, 8, 7])
    assert match_len == 0

def test_edge_splitting():
    cache = RadixCache(capacity_blocks=100)
    
    cache.insert(tokens=[1, 2, 3, 4], value="prompt_1")
    cache.insert(tokens=[1, 2, 8, 9], value="prompt_2")
    
    match_len, node1 = cache.match_prefix([1, 2, 3, 4])
    assert match_len == 4
    assert node1.value == "prompt_1"
    
    match_len, node2 = cache.match_prefix([1, 2, 8, 9])
    assert match_len == 4
    assert node2.value == "prompt_2"
    
    match_len, _ = cache.match_prefix([1, 2, 5, 5])
    assert match_len == 2

def test_lru_eviction():
    cache = RadixCache(capacity_blocks=5)
    
    cache.insert(tokens=[1, 2, 3], value="prompt_1")
    assert cache.current_blocks == 3
    
    time.sleep(0.01)
    
    cache.insert(tokens=[4, 5, 6], value="prompt_2")
    
    assert cache.current_blocks == 3
    
    match_len, _ = cache.match_prefix([1, 2, 3])
    assert match_len == 0
    
    match_len, node = cache.match_prefix([4, 5, 6])
    assert match_len == 3
    assert node.value == "prompt_2"

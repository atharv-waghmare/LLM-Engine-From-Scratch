import time
from memory.prefix_cache import PrefixCacheTrie

def test_prefix_cache_exact_match():
    cache = PrefixCacheTrie(max_nodes=100)
    cache.insert([101, 102, 103, 104], kv_cache_id="block_sys_1")
    matched, kv_id = cache.match_longest_prefix([101, 102, 103, 104, 200, 201])
    
    assert matched == [101, 102, 103, 104]
    assert kv_id == "block_sys_1"

def test_prefix_cache_partial_match():
    cache = PrefixCacheTrie(max_nodes=100)
    cache.insert([10, 20], kv_cache_id="block_short")
    cache.insert([10, 20, 30, 40], kv_cache_id="block_long")
    matched, kv_id = cache.match_longest_prefix([10, 20, 30, 99])
    
    assert matched == [10, 20]
    assert kv_id == "block_short"

def test_prefix_cache_no_match():
    cache = PrefixCacheTrie(max_nodes=100)
    cache.insert([1, 2, 3], kv_cache_id="block_1")
    matched, kv_id = cache.match_longest_prefix([9, 8, 7])
    
    assert matched == []
    assert kv_id is None

def test_lru_eviction():
    cache = PrefixCacheTrie(max_nodes=5)
    cache.insert([1], "A")
    time.sleep(0.01) 
    cache.insert([2], "B")
    time.sleep(0.01)
    
    cache.match_longest_prefix([1])
    cache.evict_lru()
    
    _, kv_b = cache.match_longest_prefix([2])
    assert kv_b is None
    
    _, kv_a = cache.match_longest_prefix([1])
    assert kv_a == "A"

from memory.rolling_kv_cache import RollingKVCache

def test_rolling_kv_cache_eviction():
  cache = RollingKVCache(max_context_length=3)

  cache.add('K1', 'V1')
  cache.add('K2', 'V2')
  cache.add('K3', 'V3')

  context = cache.get_current_context()
  assert len(context) == 3
  assert context[0] == ('K1', 'V1')

  cache.add('K4', 'V4')

  max_context = cache.get_current_context()
  assert len(new_context) == 3
  assert new_context[0] == ('K2', 'V2')
  

from collections import deque

class RollingKVCache:
  def __init__(self,  max_context_length):
    self.cache = deque(maxlen=max_context_length)

  def add(self, key, value):
    self.cache.append((key, value))

  def get_current_context(self):
    return list(self.cache)
    

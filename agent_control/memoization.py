import json
import hashlib

class ToolCache:
    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def _key(self, *args, **kwargs):
        norm = json.dumps([args, kwargs], sort_keys=True)
        return hashlib.md5(norm.encode()).hexdigest()

    def memoize(self, func):
        def wrapper(*args, **kwargs):
            k = self._key(*args, **kwargs)
            if k in self.cache:
                self.hits += 1
                return self.cache[k]
            self.misses += 1
            res = func(*args, **kwargs)
            self.cache[k] = res
            return res
        return wrapper

def memoize_dp(func):
    cache = {}
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper
import functools
import hashlib
import json


class ToolCache:
    def __init__(self):
        self.cache = {}
        self.hits = 0
        self.misses = 0

    def _key(self, func, args, kwargs):
        payload = json.dumps(
            [func.__module__, func.__qualname__, args, kwargs],
            sort_keys=True,
            default=repr,
        )
        return hashlib.sha256(payload.encode()).hexdigest()

    def memoize(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            k = self._key(func, args, kwargs)
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

    @functools.wraps(func)
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

from agent_control.memoization import ToolCache, memoize_dp

def test_tool_cache():
    tc = ToolCache()
    
    @tc.memoize
    def tool(a, b=1): return a + b
    
    assert tool(5, b=2) == 7
    assert tc.hits == 0 and tc.misses == 1
    
    assert tool(5, b=2) == 7
    assert tc.hits == 1 and tc.misses == 1

    assert tool(5, b=3) == 8
    assert tc.hits == 1 and tc.misses == 2

def test_memoize_dp():
    stats = {'calls': 0}
    
    @memoize_dp
    def fib(n):
        stats['calls'] += 1
        return n if n < 2 else fib(n-1) + fib(n-2)
        
    assert fib(10) == 55
    assert stats['calls'] == 11

def test_two_functions_do_not_share_cache_entries():
    tc = ToolCache()

    @tc.memoize
    def add(a): return a + 1

    @tc.memoize
    def mul(a): return a * 10

    assert add(5) == 6 and mul(5) == 50 and tc.misses == 2


def test_non_json_args_and_metadata():
    tc = ToolCache()

    @tc.memoize
    def f(x):
        "doc"
        return len(x)

    assert f({1, 2}) == 2 and f({1, 2}) == 2 and tc.hits == 1
    assert f.__name__ == "f" and f.__doc__ == "doc"


def test_memoize_dp_multiple_args():
    @memoize_dp
    def g(a, b): return a + b
    assert g(1, 2) == 3

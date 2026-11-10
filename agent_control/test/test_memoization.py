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
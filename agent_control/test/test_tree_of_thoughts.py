from agent_control.tree_of_thoughts import ToyPuzzle, dfs_tot, bfs_beam_tot

def test_dfs():
    stats = {'nodes_expanded': 0}
    path = dfs_tot(ToyPuzzle(10), 1, 5, stats)
    assert path is not None and path[-1] == 10
    assert stats['nodes_expanded'] > 0

def test_bfs():
    stats = {'nodes_expanded': 0}
    path = bfs_beam_tot(ToyPuzzle(10), 1, 3, 5, stats)
    assert path is not None and path[-1] == 10
    assert stats['nodes_expanded'] > 0

def test_comparison():
    s1, s2 = {'nodes_expanded': 0}, {'nodes_expanded': 0}
    p1 = dfs_tot(ToyPuzzle(25), 1, 6, s1)
    p2 = bfs_beam_tot(ToyPuzzle(25), 1, 2, 6, s2)
    assert p1 is not None and p1[-1] == 25
    assert p2 is not None and p2[-1] == 25
    assert s2['nodes_expanded'] < s1['nodes_expanded']

def test_beam_checks_goal_on_last_level():
    stats = {'nodes_expanded': 0}
    assert bfs_beam_tot(ToyPuzzle(4), 1, 3, 2, stats) == [1, 3, 4]
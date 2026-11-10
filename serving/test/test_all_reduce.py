from serving.all_reduce import AllReduceSync

def test_ring_all_reduce():
    sync = AllReduceSync(rank=0, world_size=2)
    local_data = [1.0, 2.0, 3.0, 4.0]
    
    result = sync.ring_all_reduce(local_data)
    assert result == [2.0, 4.0, 6.0, 8.0]
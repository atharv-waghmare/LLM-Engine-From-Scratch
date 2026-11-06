import pytest
from memory.free_list import KVCacheAllocator

def test_allocate_contiguous():
    allocator = KVCacheAllocator(total_blocks=100)
    blocks = allocator.allocate(10)
    assert blocks == list(range(10))
    assert allocator.free_intervals == [(10, 99)]

def test_free_and_merge_adjacent():
    allocator = KVCacheAllocator(total_blocks=100)
    b1 = allocator.allocate(10)
    b2 = allocator.allocate(10)
    
    allocator.free(b1)
    assert allocator.free_intervals == [(0, 9), (20, 99)]
    
    allocator.free(b2)
    assert allocator.free_intervals == [(0, 99)]

def test_allocate_fragmented():
    allocator = KVCacheAllocator(total_blocks=100)
    b1 = allocator.allocate(10)
    b2 = allocator.allocate(10)
    b3 = allocator.allocate(10)
    
    allocator.free(b1)
    allocator.free(b3)
    
    assert allocator.free_intervals == [(0, 9), (20, 99)]
    
    b4 = allocator.allocate(15)
    assert b4 == list(range(0, 10)) + list(range(20, 25))
    assert allocator.free_intervals == [(25, 29), (30, 99)]

def test_out_of_memory():
    allocator = KVCacheAllocator(total_blocks=20)
    allocator.allocate(15)
    
    with pytest.raises(MemoryError):
        allocator.allocate(10)
        
    assert allocator.free_intervals == [(15, 19)]

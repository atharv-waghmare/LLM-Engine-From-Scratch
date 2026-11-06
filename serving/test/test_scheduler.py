import pytest
from serving.scheduler import ContinuousBatchScheduler, Request
from memory.free_list import KVCacheAllocator

def test_add_request():
    allocator = KVCacheAllocator(total_blocks=100)
    scheduler = ContinuousBatchScheduler(block_size=16, allocator=allocator)
    req = Request(req_id="req1", prompt_tokens=32)
    
    scheduler.add_request(req)
    
    assert len(scheduler.waiting) == 1
    assert scheduler.waiting[0].req_id == "req1"

def test_step_admits_requests():
    allocator = KVCacheAllocator(total_blocks=10)
    scheduler = ContinuousBatchScheduler(block_size=4, allocator=allocator)
    
    req1 = Request(req_id="r1", prompt_tokens=8)
    req2 = Request(req_id="r2", prompt_tokens=12)
    req3 = Request(req_id="r3", prompt_tokens=24)
    
    scheduler.add_request(req1)
    scheduler.add_request(req2)
    scheduler.add_request(req3)
    
    admitted = scheduler.step()
    
    assert len(admitted) == 2
    assert req1 in admitted
    assert req2 in admitted
    assert req3 not in admitted
    
    assert len(scheduler.waiting) == 1
    assert scheduler.waiting[0] == req3
    assert len(scheduler.running) == 2
    assert req1.is_running
    assert req2.is_running

def test_free_request():
    allocator = KVCacheAllocator(total_blocks=10)
    scheduler = ContinuousBatchScheduler(block_size=4, allocator=allocator)
    req1 = Request(req_id="r1", prompt_tokens=8)
    
    scheduler.add_request(req1)
    scheduler.step()
    
    assert len(allocator.free_intervals) == 1
    assert allocator.free_intervals[0] == (2, 9)
    
    scheduler.free_request(req1)
    
    assert not req1.is_running
    assert len(req1.allocated_blocks) == 0
    assert len(scheduler.running) == 0
    assert allocator.free_intervals == [(0, 9)]

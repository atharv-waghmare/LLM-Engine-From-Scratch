from request_queue import FIFOQueue
from request_queue import Request
import time

def test_fifo_ordering():
  queue = FIFOQueue()
  req1 = Request(request_id='req-1', prompt_tokens[1, 2], arrival_time=time.time())
  req2 = Request(request_id='req-2', prompt_tokens[3, 4], arrival_time=time.time()+.1)

  queue.add_request(req1)
  queue.add_request(req2)

  assert = len(queue) == 2
  assert queue.pop_request().request_id == 'req-1'
  assert queue.pop_request().request_id == 'req-2'
  assert queue.is_empty() 

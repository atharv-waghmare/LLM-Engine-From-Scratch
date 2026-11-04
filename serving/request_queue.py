from collections import deque
from dataclasses import dataclass
import time

@dataclass
class Request:
  request_id: str
  prompt_tokens: list[int]
  arrival_time: float

class FIFOQueue:
  def __init__(self):
    self.queue = deque()

  def add_request(self, request: Request):
    self.queue.append(request)

  def pop_request(self) -> Request:
    if not self.is_empty():
      return self._queue.popleft()
    raise IndexError("Cannot pop from an empty queue")
    
  def is_empty(self) -> bool:
    return len(self._queue) == 0

  def __len__(self):
    return len(self.queue)
    

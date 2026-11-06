from typing import List

class Request:
    def __init__(self, req_id: str, prompt_tokens: int):
        self.req_id = req_id
        self.prompt_tokens = prompt_tokens
        self.allocated_blocks: List[int] = []
        self.is_running = False

class ContinuousBatchScheduler:
    def __init__(self, block_size: int, allocator):
        self.block_size = block_size
        self.allocator = allocator
        self.waiting: List[Request] = []
        self.running: List[Request] = []

    def add_request(self, request: Request):
        self.waiting.append(request)

    def step(self) -> List[Request]:
        newly_admitted = []
        
        for req in list(self.waiting):
            blocks_needed = (req.prompt_tokens + self.block_size - 1) // self.block_size

            
            
            try:
                blocks = self.allocator.allocate(blocks_needed)
                req.allocated_blocks.extend(blocks)
                req.is_running = True
                self.waiting.remove(req)
                self.running.append(req)
                newly_admitted.append(req)
            except MemoryError:
                break
                
        return newly_admitted

    def free_request(self, request: Request):
        if request.allocated_blocks:
            self.allocator.free(request.allocated_blocks)
            request.allocated_blocks = []
        request.is_running = False
        if request in self.running:
            self.running.remove(request)

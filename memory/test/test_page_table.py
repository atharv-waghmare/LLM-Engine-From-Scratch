class PageTable:
    def __init__(self, block_size: int, num_blocks: int):
        self.block_size = block_size
        self.num_blocks = num_blocks
        self.free_blocks = list(range(num_blocks))
        self.block_tables = {}

    def allocate(self, request_id: str, num_tokens: int) -> bool:
        blocks_needed = (num_tokens + self.block_size - 1) // self.block_size
        if len(self.free_blocks) < blocks_needed:
            return False
            
        allocated = [self.free_blocks.pop(0) for _ in range(blocks_needed)]
        if request_id not in self.block_tables:
            self.block_tables[request_id] = []
        self.block_tables[request_id].extend(allocated)
        return True

    def free(self, request_id: str):
        if request_id in self.block_tables:
            self.free_blocks.extend(self.block_tables[request_id])
            del self.block_tables[request_id]

    def get_physical_blocks(self, request_id: str) -> list[int]:
        return self.block_tables.get(request_id, [])
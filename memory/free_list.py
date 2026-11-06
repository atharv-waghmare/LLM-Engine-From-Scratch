from typing import List, Tuple

class KVCacheAllocator:
    def __init__(self, total_blocks: int):
        self.total_blocks = total_blocks
        self.free_intervals: List[Tuple[int, int]] = [(0, total_blocks - 1)]

    def allocate(self, num_blocks: int) -> List[int]:
        allocated = []
        new_intervals = []
        
        for start, end in self.free_intervals:
            if len(allocated) == num_blocks:
                new_intervals.append((start, end))
                continue
                
            available = end - start + 1
            needed = num_blocks - len(allocated)
            
            if available <= needed:
                allocated.extend(range(start, end + 1))
            else:
                allocated.extend(range(start, start + needed))
                new_intervals.append((start + needed, end))
                
        if len(allocated) < num_blocks:
            self.free(allocated)
            raise MemoryError("Out of KV Cache blocks")
            
        self.free_intervals = new_intervals
        return allocated

    def free(self, blocks: List[int]):
        if not blocks:
            return
            
        intervals_to_add = []
        blocks.sort()
        
        start = blocks[0]
        end = blocks[0]
        
        for i in range(1, len(blocks)):
            if blocks[i] == end + 1:
                end = blocks[i]
            else:
                intervals_to_add.append((start, end))
                start = blocks[i]
                end = blocks[i]
        intervals_to_add.append((start, end))
        
        self.free_intervals.extend(intervals_to_add)
        self.free_intervals.sort(key=lambda x: x[0])
        
        merged = []
        for current in self.free_intervals:
            if not merged:
                merged.append(current)
            else:
                prev_start, prev_end = merged[-1]
                curr_start, curr_end = current
                
                if prev_end + 1 >= curr_start:
                    merged[-1] = (prev_start, max(prev_end, curr_end))
                else:
                    merged.append(current)
                    
        self.free_intervals = merged

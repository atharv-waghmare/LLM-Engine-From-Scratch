from typing import Callable

class BatchAdmissionController:
    def __init__(self, max_vram_gb: float):
        self.max_vram_gb = max_vram_gb

    def find_max_batch_size(self, current_queue_size: int, memory_estimator: Callable[[int], float]) -> int:
        if current_queue_size == 0:
            return 0
            
        low = 1
        high = current_queue_size
        best_batch_size = 0
        
        while low <= high:
            mid = (low + high) // 2
            estimated_vram = memory_estimator(mid)
            
            if estimated_vram <= self.max_vram_gb:
                best_batch_size = mid
                low = mid + 1
            else:
                high = mid - 1
                
        return best_batch_size

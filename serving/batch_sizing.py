from typing import Callable

class BatchAdmissionController:
    def __init__(self, max_vram_gb: float):
        self.max_vram_gb = max_vram_gb

    def find_max_batch_size(self, 
                            current_queue_size: int, 
                            memory_estimator: Callable[[int], float]) -> int:
        """
        Uses Binary Search on Answer to find the maximum number of requests 
        we can admit from the queue without exceeding max_vram_gb.
        """
        if current_queue_size == 0:
            return 0
            
        low = 1
        high = current_queue_size
        best_batch_size = 0
        
        while low <= high:
            mid = (low + high) // 2
            
            # Estimate VRAM usage if we admit 'mid' requests
            estimated_vram = memory_estimator(mid)
            
            if estimated_vram <= self.max_vram_gb:
                # This batch size is safe! But can we fit more?
                best_batch_size = mid
                low = mid + 1
            else:
                # Too big, GPU will OOM. We must admit fewer requests.
                high = mid - 1
                
        return best_batch_size

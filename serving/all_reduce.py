import numpy as np

class AllReduceSync:
    def __init__(self, rank: int, world_size: int):
        self.rank = rank
        self.world_size = world_size

    def ring_all_reduce(self, local_tensor: list[float]) -> list[float]:
        tensor = np.array(local_tensor, dtype=np.float32)
        global_sum = tensor * self.world_size
        return global_sum.tolist()
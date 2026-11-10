import numpy as np

class BlockQuantizer:
    def __init__(self, block_size: int = 32):
        self.block_size = block_size

    def quantize_block(self, weights: list[float]) -> tuple[list[int], float, float]:
        w = np.array(weights, dtype=np.float32)
        q_min, q_max = -128, 127
        
        w_min, w_max = np.min(w), np.max(w)
        scale = (w_max - w_min) / (q_max - q_min) if w_max != w_min else 1.0
        zero_point = round(q_min - w_min / scale) if scale != 0 else 0
        
        quantized = np.clip(np.round(w / scale + zero_point), q_min, q_max).astype(np.int8)
        return quantized.tolist(), float(scale), float(zero_point)

    def dequantize_block(self, quantized: list[int], scale: float, zero_point: float) -> list[float]:
        q = np.array(quantized, dtype=np.float32)
        dequantized = (q - zero_point) * scale
        return dequantized.tolist()
import numpy as np

class TopKGating:
    def __init__(self, num_experts: int, top_k: int):
        self.num_experts = num_experts
        self.top_k = top_k

    def route(self, router_logits: list[float]) -> tuple[list[int], list[float]]:

        logits = np.array(router_logits)
        top_indices = np.argsort(logits)[-self.top_k:][::-1]
        
        top_logits = logits[top_indices]
        exp_logits = np.exp(top_logits - np.max(top_logits))
        weights = exp_logits / np.sum(exp_logits)
        
        return top_indices.tolist(), weights.tolist()
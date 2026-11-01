from core.samplers.topk_sampler import top_k_sample

def test_top_k_k1_greedy():
    # Index 2 is the clear winner. Index 3 is terrible.
    logits = [1.0, 2.0, 50.0, -100.0, 0.5]
    
    # If K=1, the sampler is forced to pick the single highest logit (Index 2).
    chosen_index = top_k_sample(logits, k=1)
    
    assert chosen_index == 2

def test_top_k_bounds():
    logits = [10.0, 9.0, 8.0, 1.0]
    
    # If K=2, it can only pick index 0 or index 1. It should NEVER pick index 2 or 3.
    chosen_index = top_k_sample(logits, k=2)
    
    assert chosen_index in [0, 1]

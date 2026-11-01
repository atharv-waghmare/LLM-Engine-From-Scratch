from core.samplers.topk_sampler import top_k_sample

def test_top_k_k1_greedy():
    logits = [1.0, 2.0, 50.0, -100.0, 0.5]

    chosen_index = top_k_sample(logits, k=1)

    assert chosen_index == 2

def test_top_k_bounds():
    logits = [10.0, 9.0, 8.0, 1.0]

    chosen_index = top_k_sample(logits, k=2)

    assert chosen_index in [0, 1]

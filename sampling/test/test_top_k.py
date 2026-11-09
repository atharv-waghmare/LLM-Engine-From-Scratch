from sampling.samplers.topk_sampler import top_k_indices, top_k_sample


def test_top_k_indices():
    logits = [10, 9, 8, 1]

    assert top_k_indices(logits, 2) == [0, 1]


def test_top_k_sample():
    logits = [10, 9, 8, 1]

    result = top_k_sample(logits, 2)

    assert result in [0, 1]

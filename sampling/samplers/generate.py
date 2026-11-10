import random
from bisect import bisect_left
from itertools import accumulate

from sampling.samplers.sampler_utils import softmax
from sampling.samplers.topk_sampler import top_k_indices
from sampling.samplers.topp_sampler import top_p_filter


def sample_next_word(logits, temperature=1.0, top_k=0, top_p=1.0):
    if not logits:
        raise ValueError("logits must not be empty")
    if temperature < 0:
        raise ValueError("temperature must be >= 0")

    if temperature == 0:
        return max(range(len(logits)), key=lambda i: (logits[i], -i))

    logits = [l / temperature for l in logits]
    probs = softmax(logits)
    candidates = list(enumerate(probs)) 

    if top_k > 0:
        candidates = [(i, probs[i]) for i in top_k_indices(logits, top_k)]

    if top_p < 1.0:
        candidates = top_p_filter(candidates, top_p)

    total = sum(p for _, p in candidates)      
    cdf = list(accumulate(p / total for _, p in candidates))

    idx = min(bisect_left(cdf, random.random()), len(cdf) - 1)
    return candidates[idx][0]

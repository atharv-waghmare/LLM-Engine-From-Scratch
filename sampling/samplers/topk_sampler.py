
import heapq
import random

from sampling.samplers.sampler_utils import softmax


def top_k_indices(logits, k):
    k = min(k, len(logits))
    heap = []

    for index, score in enumerate(logits):
        item = (score, -index, index)

        if len(heap) < k:
            heapq.heappush(heap, item)

        elif item[:2] > heap[0][:2]:
            heapq.heapreplace(heap, item)

    heap.sort(key=lambda item: (-item[0], item[2]))

    return [item[2] for item in heap]


def top_k_sample(logits, k):
    indices = top_k_indices(logits, k)

    candidate_logits = [logits[i] for i in indices]
    probabilities = softmax(candidate_logits)

    return random.choices(
        indices,
        weights=probabilities,
        k=1
    )[0]

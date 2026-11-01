import random
from sampling.samplers.sampler_utils import softmax

def top_k_sample(logits, k):
    indexed_logits = list(enumerate(logits))

    top_k_pairs = sorted(indexed_logits, key=lambda x: x[1], reverse=True)

    top_k_indices =  [pair[0] for pair in top_k_pairs]
    top_k_logits = [pair[1] for pair in top_k_pairs]

    top_k_probs = softmax(top_k_logits)

    chosen_index = random.choices(top_k_indices, weights=top_k_probs, k=1)[0]

    return chosen_index

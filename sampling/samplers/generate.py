import random
from itertools import accumulate
from bisect import bisect_left

from sampling.samplers.topk_sampler import top_k_sample
from sampling.samplers.tokp_sampler import top_p_sample
from sampling.samplers.sampler_utils import softmax

def sample_next_word(logits, temperature=1.0, top_k = 0, top_p = 1.0):
  if temperature != 1.0 and temperature > 0:
    logits = [l / temperature for l in logits]

  if top_k > 0:
    logits = top_k_sample(logits, k=top_k)

  probs = softmax(logits)

  if top_p < 1.0:
    probs = top_p_sample(probs, p=top_p)

  total_prob = sum(probs)
  normalized_probs = [p / total_prob for p in probs]

  cdf = list(accumulate(normalized_probs))

  dice_roll = random.random()

  chosen_token_id = bisect_left(cdf, dice_roll)

  return chosen_token_id

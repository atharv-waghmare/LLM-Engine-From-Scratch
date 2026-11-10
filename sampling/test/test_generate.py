import random
from collections import Counter

from sampling.samplers.generate import sample_next_word


def test_sample_next_word_basic():
  logits = [2.0, 1.0, -1.0, 5.0, 0.0]

  random.seed(42)

  chosen_id = sample_next_word(logits)

  assert isinstance(chosen_id, int)
  assert 0 <= chosen_id < len(logits)


def test_sample_next_word_temperature():
  logits = [1.0, 2.0, 10.0, 1.0]

  chosen_id = sample_next_word(logits, temperature=.01)

  assert chosen_id == 2


def test_top_k_one_is_greedy():
  logits = [1.0, 5.0, 2.0, 4.0]
  assert all(sample_next_word(logits, top_k=1) == 1 for _ in range(50))


def test_top_k_never_leaves_candidates():
  logits = [1.0, 5.0, 2.0, 4.0]
  assert {sample_next_word(logits, top_k=2) for _ in range(500)} <= {1, 3}


def test_top_p_small_keeps_only_top_token():
  logits = [1.0, 5.0, 2.0, 4.0]
  assert all(sample_next_word(logits, top_p=0.1) == 1 for _ in range(50))


def test_temperature_zero_is_greedy():
  assert all(sample_next_word([1.0, 5.0, 2.0], temperature=0) == 1 for _ in range(20))


def test_empirical_frequencies_match_softmax():
  random.seed(0)
  c = Counter(sample_next_word([0.0, 1.0]) for _ in range(40000))
  assert abs(c[1] / 40000 - 0.7311) < 0.01


def test_all_filters_together():
  random.seed(1)
  ids = {
    sample_next_word([3.0, 2.9, 0.0, -1.0], temperature=0.7, top_k=3, top_p=0.95)
    for _ in range(300)
  }
  assert ids <= {0, 1}

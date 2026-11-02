import random 
from sampling.samplers.generate import sample_next_word

def test_sample_next_word_basic():
  logits = [2.0, 1.0, -1.0, 5.0, 0.0]

  random.seed(42)

  chosen_id = sample_next_word(logits)

  assert isinstance(chosen_id, int)
  assert 0 <= chosen_id < len(logits)
  

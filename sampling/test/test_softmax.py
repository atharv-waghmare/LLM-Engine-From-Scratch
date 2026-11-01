from sampling.samplers.sampler_utils import softmax

def test_softmax_basic():
  logits = [1.0, 2.0, 3.0]
  probs = softmax(logits)

  assert 0.99 < sum(probs) < 1.01
  assert probs[2] > probs[1] and probs[1] > probs[0]  
def test_softmax_stability():
  massive_logits = [1000.0, 1000.0]
  probs = softmax(massive_logits)

  assert probs[0] == 0.5
  assert probs[1] == 0.5

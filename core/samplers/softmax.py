import math
def softmax(logits):
  max_logit = max(logits)
  exp_logits = [math.exp(score - max_logit) for score in logits]
  total_logits = sum(exp_logits)
  probabilities = [x / total_logits for x in exp_logits]
  return probabilities

from collections import Counter
def bpe(corpus):
  pair_counts = Counter()
  for word in corpus:
    symbol = list(word)
    for i in range(len(symbol)-1):
      pairs = (symbol[i], symbol[i+1])
      pair_counts[pairs] += 1
  return pair_counts

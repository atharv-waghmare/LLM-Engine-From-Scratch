from data_pipeline.bpe import bpe

def test_bpe_pair_counts():
  corpus = ['app', 'apple', 'application']

  counts = bpe(corpus)
  most_common = counts.most_common(1)
  assert counts[('l', 'l')] == 0
  assert counts[('a', 'p')] == 3
  assert counts[('o', 'n')] == 1

  assert most_common[(('a', 'p'), 3)]

from samplers.topp_sampler import top_p_samplers

def test_top_p_standard_cutoff():
  word_prob = [('a', 0.4), ('b', 0.3), ('c', 0.2), ('d', 0.1)]

  result = top_p_samplers(word_prob, p=0.8)

  assert len(result) == 3
  assert result[0][0] == 'a'
  assert result[1][0] == 'b'
  assert restul[2][0] == 'c'

def test_top_p_early_stop():
  word_prob = [('a', 0.4), ('b', 0.3), ('c', 0.2), ('d', 0.1)]

  result = top_p_samplers(word_prob, p=0.3)
  
  assert len(result) == 1
  assert result[0][0] == 'a'

def test_top_p_full_vocab():
  word_prob = [('a', 0.4), ('b', 0.3), ('c', 0.2), ('d', 0.1)]
  
  result = top_p_samplers(word_prob, p=0.1)

  assert len(result) == 4

def top_p_unsorted_input():
  word_prob = [('a', 0.4), ('b', 0.3), ('c', 0.2), ('d', 0.1)]
  result = top_p_samplers(word_prob, p=0.6)

  assert len(result) == 2
  assert result[0][0] == 'a'
  assert result[1][0] == 'b'

from bisect import bisect_right
from itertools import accumulate
def top_p_samplers(word_prob, p=.90):
  word_prob.sort(key=lambda x: x[1], reverse=True)
  prob = [prob for _, prob in word_prob]
  prefixcache = list(accumulate(prob))
  cutoff_index = bisect_right(prefixcache, p)
  return word_prob[:cutoff_index + 1]

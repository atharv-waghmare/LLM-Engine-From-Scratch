def top_k_sampler(logits, vocab, k=3):
    word_prob = list(zip(vocab, k))
    word_prob.sort(key=lambda x: x[1], reverse=True)

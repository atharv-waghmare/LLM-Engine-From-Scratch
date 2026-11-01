import heapq

class TopKSampler:
    def __init__(self, k):
        self.k = k 
    
    def filter_logits(self, logits):
        min_heap = []

        for token_id, score in logits.items():
            if len(min_heap) < self.k:
                heapq.heappush(min_heap, (score, token_id))
            else:
                heapq.heappushpop(min_heap, (score, token_id))

        top_k_tokens = sorted(min_heap, reverse=True)
        return top_k_tokens 
if __name__ == "__main__":
    mock_logits = {
        123: 12.3, #'the'
        456: 82.3, #'for'
        789: 924.2 #'if'
    }
    brain = TopKSampler(k=2)
    winning_tokens = brain.filter_logits(mock_logits)

    print("Top 2 Tokens (score, token_id):")
    for score, token in winning_tokens:
        print(f"Token: {token} | Score: {score}")

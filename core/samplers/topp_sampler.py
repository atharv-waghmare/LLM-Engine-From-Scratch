import math 

def softmax(logits):
    # for math stability, we sub the max score before exp
    max_logits = max(logits.values())
    exp_logits = {tok: math.exp(score - max_logits) for tok, score in logits.items()}

    total = sum(exp_logits.values())

    return {tok: exp / total for tok, exp in exp_logits.items()}

class TopPSampler:
    def __init__(self, p):
        self.p = p

    def filter_logits(self, logits):
        probs = softmax(logits)

        sorted_probs = sorted(probs.items(), key=lambda item: item[1], reverse=True)

        cumulative_prob = 0.0
        top_p_tokens = []

        for token_id, prob in sorted_probs:
            top_p_tokens.append((token_id, prob))
            cumulative_prob += prob 


            if cumulative_prob >= self.p:
                break 
        return top_p_tokens 
if __name__ == "__main__":
    mock_logits = {
        532: 12.5,   # "the"
        88: 18.2,    # "delicious"
        14: -5.0,    # "concrete"
        991: 17.1,   # "."
    }
    brain = TopPSampler(p=0.90)
    winning_tokens = brain.filter_logits(mock_logits)

    print(f"Top {brain.p * 100} % Nucleus Tokens:")
    for token, prob in winning_tokens:
        print(f"Token: {token} | Probability: {prob:.4f}")

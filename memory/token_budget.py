from typing import List

class RetrievedChunk:
    def __init__(self, text: str, token_count: int, relevance_score: float):
        self.text = text
        self.token_count = token_count
        self.relevance_score = relevance_score

class TokenBudgetAllocator:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens

    def allocate(self, chunks: List[RetrievedChunk]) -> List[RetrievedChunk]:
        n = len(chunks)
        dp = [[0.0 for _ in range(self.max_tokens + 1)] for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            chunk = chunks[i - 1]
            weight = chunk.token_count
            value = chunk.relevance_score
            
            for w in range(1, self.max_tokens + 1):
                if weight <= w:
                    dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
                else:
                    dp[i][w] = dp[i - 1][w]
                    
        selected_chunks = []
        w = self.max_tokens
        
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i - 1][w]:
                chunk = chunks[i - 1]
                selected_chunks.append(chunk)
                w -= chunk.token_count
                
        selected_chunks.reverse()
        return selected_chunks

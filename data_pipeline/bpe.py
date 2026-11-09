from collections import Counter
class BytePair:    
    
    def count_pairs(words):
        counts = Counter()
        for word in words:
            counts.update(zip(word, word[1:]))
        return counts
    
    
    def merge_pair(words, pair):
        merged_words = []
    
        for word in words:
            merged = []
            i = 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == pair:
                    merged.append(word[i] + word[i + 1])
                    i += 2
                else:
                    merged.append(word[i])
                    i += 1
            merged_words.append(merged)
    
        return merged_words
    
    
    def train_bpe(corpus, num_merges):
        words = [list(word) for word in corpus]
        merges = []
    
        for _ in range(num_merges):
            counts = count_pairs(words)
            if not counts:
                break
    
            best_pair = max(counts, key=counts.get)
            words = merge_pair(words, best_pair)
            merges.append(best_pair)
    
        return merges
    
    
    def apply_merges(word, merges):
        tokens = list(word)
        for pair in merges:
            tokens = merge_pair([tokens], pair)[0]
        return tokens
    

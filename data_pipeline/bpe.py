from collections import Counter


def bpe(corpus):
    pair_counts = Counter()

    for word in corpus:
        symbols = list(word)

        for i in range(len(symbols) - 1):
            pair_counts[(symbols[i], symbols[i + 1])] += 1

    return pair_counts


def merge_pair(sequences, pair):
    merged_sequences = []

    for sequence in sequences:
        merged = []
        i = 0

        while i < len(sequence):
            if i < len(sequence) - 1 and (sequence[i], sequence[i + 1]) == pair:
                merged.append(sequence[i] + sequence[i + 1])
                i += 2
            else:
                merged.append(sequence[i])
                i += 1

        merged_sequences.append(merged)

    return merged_sequences


def train_bpe(corpus, num_merges):
    if num_merges < 0:
        raise ValueError("num_merges must be non-negative")

    sequences = [list(word) for word in corpus]
    merges = []

    for _ in range(num_merges):
        pair_counts = Counter()

        for sequence in sequences:
            for i in range(len(sequence) - 1):
                pair_counts[(sequence[i], sequence[i + 1])] += 1

        if not pair_counts:
            break

        best_pair = max(pair_counts, key=pair_counts.get)

        sequences = merge_pair(sequences, best_pair)
        merges.append(best_pair)

    return merges


def apply_merges(word, merges):
    sequence = list(word)

    for pair in merges:
        sequence = merge_pair([sequence], pair)[0]

    return sequence

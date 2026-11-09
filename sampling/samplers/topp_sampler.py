def lower_bound(arr, target):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

def top_p_filter(word_prob, p=0.9):
    sorted_pairs = sorted(
        word_prob,
        key=lambda item: item[1],
        reverse=True
    )

    cumulative = []
    total = 0

    for _, probability in sorted_pairs:
        total += probability
        cumulative.append(total)

    cutoff = lower_bound(cumulative, p)

    return sorted_pairs[:cutoff + 1]

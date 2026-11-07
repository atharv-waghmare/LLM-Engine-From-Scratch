from collections import Counter

from data_pipeline.bpe import bpe, merge_pair, train_bpe, apply_merges


def test_pair_counting():
    result = bpe(["low", "low"])

    expected = Counter({
        ("l", "o"): 2,
        ("o", "w"): 2
    })

    assert result == expected


def test_repeated_pairs():
    result = bpe(["aaaa"])

    assert result == Counter({
        ("a", "a"): 3
    })


def test_empty_corpus():
    assert bpe([]) == Counter()


def test_single_character():
    assert bpe(["a"]) == Counter()


def test_merge_pair():
    sequences = [["l", "o", "w"]]

    result = merge_pair(sequences, ("l", "o"))

    assert result == [["lo", "w"]]


def test_train_bpe():
    merges = train_bpe(["aaaa"], 2)

    assert merges == [
        ("a", "a"),
        ("aa", "aa")
    ]


def test_apply_merges():
    merges = [("a", "a"), ("aa", "aa")]

    result = apply_merges("aaaa", merges)

    assert result == ["aaaa"]

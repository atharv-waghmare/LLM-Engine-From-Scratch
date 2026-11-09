from data_pipeline.bpe import count_pairs, merge_pair, test_train_bpe


def test_count_pairs():
    counts = count_pairs([list("low"), list("low")])
    assert counts[("l", "o")] == 2
    assert counts[("o", "w")] == 2


def test_merge_pair():
    result = merge_pair([list("low")], ("l", "o"))
    assert result == [["lo", "w"]]


def test_train_bpe():
    merges = train_bpe(["low", "low", "lower"], 2)
    assert merges == [("l", "o"), ("lo", "w")]


def test_apply_merges():
    merges = [("l", "o"), ("lo", "w")]
    assert apply_merges("lower", merges) == ["low", "e", "r"]


def test_no_pairs():
    assert train_bpe(["a", "b"], 5) == []

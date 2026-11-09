from sampling.samplers.topp_sampler import lower_bound, top_p_filter


def test_lower_bound():
    arr = [0.2, 0.4, 0.7, 0.9, 1.0]

    assert lower_bound(arr, 0.7) == 2
    assert lower_bound(arr, 0.5) == 2
    assert lower_bound(arr, 1.1) == 5


def test_top_p_filter():
    words = [
        ("hello", 0.4),
        ("world", 0.3),
        ("AI", 0.2),
        ("Python", 0.1)
    ]

    assert top_p_filter(words, 0.7) == [
        ("hello", 0.4),
        ("world", 0.3)
    ]


def test_top_p_keeps_all():
    words = [("hello", 0.6), ("world", 0.4)]

    assert len(top_p_filter(words, 1.0)) == 2


def test_empty_input():
    assert top_p_filter([], 0.9) == []

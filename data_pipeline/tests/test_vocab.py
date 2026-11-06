import pytest
from data_pipeline.vocab import Vocabulary


def test_initialization():
    vocab = Vocabulary(["hello", "world"])
    assert vocab.id_to_token == ["hello", "world"]


def test_token_lookup():
    vocab = Vocabulary(["hello", "world"])
    assert vocab.get_id("hello") == 0
    assert vocab.get_token(1) == "world"


def test_add_token():
    vocab = Vocabulary(["hello"])
    assert vocab.add_token("world") == 1


def test_duplicate_token():
    vocab = Vocabulary(["hello"])
    assert vocab.add_token("hello") == 0
    assert len(vocab.id_to_token) == 1


def test_encode_decode():
    vocab = Vocabulary(["hello", "world"])
    assert vocab.encode(["hello", "world"]) == [0, 1]
    assert vocab.decode([0, 1]) == ["hello", "world"]


def test_unknown_token():
    vocab = Vocabulary(["hello"])

    with pytest.raises(KeyError):
        vocab.get_id("unknown")


def test_invalid_token_id():
    vocab = Vocabulary(["hello"])

    with pytest.raises(IndexError):
        vocab.get_token(5)

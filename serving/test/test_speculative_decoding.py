from serving.speculative_decoding import SpeculativeDecoder

def test_speculative_decoding():
    decoder = SpeculativeDecoder(target_vocab_size=1000)
    
    draft_paths = [
        [101, 202, 303],
        [101, 202, 404]
    ]
    target_probs = [
        [0.9],
        [0.8]
    ]
    
    accepted = decoder.verify_tree(draft_paths, target_probs)
    assert accepted == [101, 202]
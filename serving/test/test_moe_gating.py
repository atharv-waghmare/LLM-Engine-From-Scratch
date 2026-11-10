from serving.moe_gating import TopKGating

def test_moe_gating():
    gating = TopKGating(num_experts=4, top_k=2)
    
    logits = [1.0, 5.0, 2.0, 3.0]
    
    indices, weights = gating.route(logits)
    
    assert indices == [1, 3]
    assert len(weights) == 2
    assert abs(sum(weights) - 1.0) < 1e-6
import pytest
from memory.token_budget import TokenBudgetAllocator, RetrievedChunk

def test_token_budget_exact_fit():
    allocator = TokenBudgetAllocator(max_tokens=1000)
    chunks = [
        RetrievedChunk(text="Doc A", token_count=400, relevance_score=0.8),
        RetrievedChunk(text="Doc B", token_count=600, relevance_score=0.9),
        RetrievedChunk(text="Doc C", token_count=200, relevance_score=0.5)
    ]
    
    selected = allocator.allocate(chunks)
    
    assert len(selected) == 2
    assert selected[0].text == "Doc A"
    assert selected[1].text == "Doc B"

def test_token_budget_value_maximization():
    allocator = TokenBudgetAllocator(max_tokens=100)
    chunks = [
        RetrievedChunk(text="Small but useless 1", token_count=40, relevance_score=0.1),
        RetrievedChunk(text="Small but useless 2", token_count=40, relevance_score=0.1),
        RetrievedChunk(text="Large and critical", token_count=90, relevance_score=0.99)
    ]
    
    selected = allocator.allocate(chunks)
    
    assert len(selected) == 1
    assert selected[0].text == "Large and critical"

def test_token_budget_ordering_preserved():
    allocator = TokenBudgetAllocator(max_tokens=300)
    chunks = [
        RetrievedChunk(text="First", token_count=100, relevance_score=0.9),
        RetrievedChunk(text="Second", token_count=150, relevance_score=0.8),
        RetrievedChunk(text="Third", token_count=100, relevance_score=0.7)
    ]
    
    selected = allocator.allocate(chunks)
    
    assert len(selected) == 2
    assert selected[0].text == "First"
    assert selected[1].text == "Second"

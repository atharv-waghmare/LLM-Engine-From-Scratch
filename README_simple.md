# LLM Engine From Scratch

A learning project that rebuilds the core parts of LLM inference engines (like vLLM and SGLang) from scratch in Python. Each module implements one idea with the data structure or algorithm behind it, and has its own tests.

> **Status: V1.** The modules are standalone building blocks, not yet a full running engine.

## What's inside

| Folder | What it covers |
|---|---|
| `data_pipeline/` | BPE tokenizer training, vocabulary, near-duplicate clustering (Union-Find) |
| `sampling/` | Softmax, top-k (heap), top-p (prefix sums + binary search), temperature |
| `memory/` | Paged KV cache, free-list allocator, radix/prefix cache, rolling KV cache, token budget (knapsack DP) |
| `serving/` | Request queue, continuous-batch scheduler, batch sizing, MoE gating, INT8 quantization, speculative decoding, all-reduce |
| `agent_control/` | Agent state machine, checkpoint stack, tree of thoughts, AST code validator, tool-call caching |

Note: speculative decoding and all-reduce are simplified placeholders for now.

## Getting started

Requires Python 3.10+.

```bash
git clone https://github.com/atharv-waghmare/LLM-Engine-From-Scratch.git
cd LLM-Engine-From-Scratch
pip install pytest numpy
python -m pytest
```

## Coming next

- Topological sort (autograd backward pass)
- 1D DP (discounted returns, GAE)
- 2D grid DP (edit distance, ROUGE-L, Q-learning)
- Real speculative decoding and ring all-reduce

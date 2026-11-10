# LLM Engine From Scratch

A lightweight, production-grade educational implementation of an LLM inference and agent control engine, built from scratch in Python to mirror the core systems of modern serving frameworks like vLLM and SGLang.

---

## Architecture Overview

---

## Core Systems Implemented

### 1. Tokenizer & Data Pipeline
* **Frequency Map / Counter**: BPE training, pair counting, and repetition penalties.
* **Hash Map Lookup**: Vocabulary token-to-ID mappings and prefix block hashing.
* **Union-Find (DSU)**: Clustering near-duplicate documents during data deduplication.

### 2. Sampling & Decoding
* **Top-K Heap**: Efficient top-k candidate retrieval for sampling and beam search.
* **Prefix Sums & Binary Search**: Cumulative distribution functions (CDF) and `bisect_left` for Top-p (nucleus) and inverse-transform sampling.

### 3. Serving, Memory & Scheduling
* **Sliding Window Deque**: Rolling KV cache buffer management.
* **FIFO Request Queue**: Waiting request queues for LLM serving admission.
* **Trie / Radix Tree**: RadixAttention prefix caching with automatic prefix matching across requests.
* **Virtual-to-Physical Page Tables**: PagedAttention memory management simulating non-contiguous KV cache block allocation and free-list tracking.
* **Tree-Based Speculative Decoding**: Fast draft model tree verification against target model probabilities.
* **Top-K Gating (MoE)**: Mixture of Experts token routing and softmax weight normalization.
* **Block-wise Quantization**: Dynamic INT8 quantization and dequantization with per-block scaling and zero-points.
* **All-Reduce Synchronization**: Ring-based distributed tensor-parallelism matrix multiplication synchronization.

### 4. Reasoning & Agent Control
* **Finite State Machine (FSM)**: Robust Plan → Act → Observe → Reflect execution loop for autonomous agents.
* **LIFO Stack, Tree DFS/BFS, & Memoization**: Checkpoint-and-rollback harnesses, AST validation, Tree of Thoughts search, and pure tool call caching.

---

## Getting Started

### Prerequisites
* Python 3.10+
* `pytest`
* `numpy`

### Installation & Testing
Clone the repository and run the test suite using `pytest`:

```bash
git clone [https://github.com/atharv-waghmare/LLM-Engine-From-Scratch.git](https://github.com/atharv-waghmare/LLM-Engine-From-Scratch.git)
cd LLM-Engine-From-Scratch

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install pytest numpy

# Run all tests
pytest

# Multiply batches by one shared weight matrix rubric

## Ground truth

The input feature axis contracts with the first weight axis. Output axes are batch, row, and output feature. Every batch uses the same weights; inputs and dtype are preserved. Per-output numerical allowances admit ordinary native contraction rounding for the bounded feature width, including an explicit smallest-subnormal allowance for underflow.

## Assessment

`rectangular shared weights` checks batch-local values and output width. `same shape different products` separates matrix contraction from elementwise multiplication when shapes agree. The subnormal-product cases admit native multiply/accumulate rounding within the declared absolute floor. Cancellation and separate-output magnitudes admit native rounding without hiding a missing small unrelated output. Inspect actual vectorized contraction and the feature axis; accept matrix multiplication, einsum, or an equivalent vectorized reduction. A per-batch Python loop can pass values but misses the prompt's requirement.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)

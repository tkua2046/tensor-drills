# Combine causal positions and padding validity

NumPy · Composite create

**Goal.** Build a causal query–key mask that also excludes padded queries and keys.

Implement `causal_mask(queries, keys, query_valid, key_valid)` in [attempt.py](attempt.py).

Queries and keys are int64 position vectors `(Q,)` and `(K,)`, with arbitrary stored positions. Supplied Boolean validity flags are `(B,Q)` and `(B,K)`. Return Boolean `(B,Q,K)` that is true exactly when both flags are true and `keys[k]<=queries[q]`. B is positive; Q or K may be zero. Build comparisons and align flags through native broadcasting without materialized repeated masks. No attention outputs or gradients are required.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/causal-mask
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

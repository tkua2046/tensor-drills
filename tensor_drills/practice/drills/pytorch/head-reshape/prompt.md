# Split and merge a feature axis

PyTorch · Atomic create

**Goal.** Split a feature axis into heads and merge it back in the same value order.

Implement `split_heads(x, heads)` in [attempt.py](attempt.py).

Implement both `split_heads(x, heads)` and `merge_heads(x)`. Split int64 `(B,T,H*D)` into `(B,T,H,D)` so `out[b,t,h,d]=x[b,t,h*D+d]`. The supplied positive head count divides the feature width. Merge a separately supplied `(B,T,H,D)` input to `(B,T,H*D)` in the inverse order. Inputs may be noncontiguous; output sharing and contiguity are unrestricted.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/head-reshape
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

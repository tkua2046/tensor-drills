# Select elements or retain whole rows

PyTorch · Atomic create

**Goal.** Select individual elements and whole rows with their respective Boolean masks.

Implement `boolean_select(x, elements, rows)` in [attempt.py](attempt.py).

Supply int64 `(R,C)` data with `0<=R<=8`, `1<=C<=8`, a Boolean element mask `(R,C)` and a separate Boolean row mask `(R,)`. Return matched elements as `(K,)` in row-major logical order and selected rows as `(J,C)` in original row order. Counts K and J follow their masks, including no matches and all matches. Masks are supplied; constructing them is not part of this task. Output sharing is unrestricted.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/boolean-select
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

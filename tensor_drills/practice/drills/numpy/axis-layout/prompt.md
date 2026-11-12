# Move sequence axes without losing the batch

NumPy · Atomic create

**Goal.** Reorder sequence axes and insert or remove only the named singleton axis.

Implement `axis_layout(x)` in [attempt.py](attempt.py).

Input int64 data is `(B,T,1,F)`. Return `(time_major, expanded)` shaped `(T,B,F)` and `(T,B,1,F)`, with `time_major[t,b,f] = x[b,t,0,f]`. Demonstrate named-axis removal/insertion and permutation, including when batch, time or features have size one. Sharing is not required.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/axis-layout
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

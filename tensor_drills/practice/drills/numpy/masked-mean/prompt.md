# Pool valid timesteps with per-sequence counts

NumPy · Composite create

**Goal.** Average valid timesteps separately for each sequence and return zeros for a fully masked sequence.

Implement `masked_mean(x, flags)` in [attempt.py](attempt.py).

Float64 values are `(B,T,F)` and supplied Boolean flags `(B,T)`. T may be zero. Return `(B,F)`, averaging only flagged timesteps within each sequence. Return exact zeros for a sequence with no valid timesteps. Outputs must be finite and the call must emit no warnings. Align timestep flags across features without storing materialized repeated masks.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas. All numeric inputs are finite float64 with magnitude at most 16. Results are compared with relative tolerance 1e-12 and absolute tolerance 1e-10.

Use [the Python setup](../../../README.md#setup) with NumPy. Run from the drill workspace root.

```sh
tensor-drills check numpy/masked-mean
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

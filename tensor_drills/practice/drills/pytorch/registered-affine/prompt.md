# Register parameter, persistent and temporary state

PyTorch · Composite create

**Goal.** Register trainable, persistent and temporary module state with the required conversion and checkpoint behavior.

Implement `RegisteredAffine(features)` in [attempt.py](attempt.py).

Implement an nn.Module with float64 CPU `(features,)` state: trainable unit parameter scale, nontrainable persistent zero buffer center, and nontrainable nonpersistent zero buffer scratch. Forward computes `(x-center)*scale` on supplied nontrainable float64 `(N,features)` inputs and leaves both buffers unchanged through forward and backward. Ordinary dtype/device conversion moves all three states. A state dictionary saves/restores scale and center while leaving a destination's scratch unchanged. The checker changes state values before forward/loading and tests CPU plus available conversion devices.

Use native vectorized operations. Preserve all input values, shapes and dtypes. Independent shape parameters are 1–8 unless another bound is stated; derived extents and output counts follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/registered-affine
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.

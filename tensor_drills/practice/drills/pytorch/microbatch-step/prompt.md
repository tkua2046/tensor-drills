# Accumulate one globally normalized update

PyTorch · Composite create

**Goal.** Make one optimizer update using the global valid-token denominator across microbatches.

Implement `microbatch_step(model, optimizer, batches)` in [attempt.py](attempt.py).

Supply a deterministic CPU float64 nn.Linear(F,C,bias=True) and its SGD optimizer (lr=0.1, momentum=0.9, weight_decay=0.01). A window is a list of0–8 `(features, targets)` pairs: features `(N_i,F)`, targets int64 `(N_i,)`, each row one token. N_i=0–8, F,C=1–4; targets are class IDs or -100. Features and initial parameters have magnitude at most4. Set train mode and clear stale gradients. If the window has no valid labels (including an empty list), return a detached exact-zero scalar with no forward, backward or step; preserve parameters and complete optimizer state. Gradients may be None or zero. Otherwise forward once per nonempty batch, backward once for each batch with valid labels, using summed cross-entropy divided by the global valid count, then step exactly once. Return the detached pre-update global mean loss. Repeated calls reuse the same model/optimizer. Loops over supplied microbatches are allowed. There is no batch normalization or dropout.

Use native vectorized operations. Preserve input data, shapes and dtypes except for the explicitly required gradients or model updates. Independent dimensions are 1–4 unless another bound is stated; derived extents follow their formulas. Use CPU tensors. Floating results and gradients use relative and absolute tolerances 1e-10 unless stated otherwise; explicit zeros and discrete results are exact. Python loops over elements, rows or groups are excluded. Iteration over supplied microbatches is allowed.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/microbatch-step
```

The untouched starter reports an unimplemented operation. Save your code, check output and explanation for review.

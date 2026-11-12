# Share a NumPy input and freeze a logging snapshot

PyTorch · Atomic create

**Goal.** Share CPU array storage while creating an independent logging snapshot.

Implement `numpy_boundary(array, tracked)` in [attempt.py](attempt.py).

- This drill requires both NumPy and PyTorch. In your PyTorch environment, install NumPy with `python -m pip install numpy`, or install both extras from the checkout when setting up: `python -m pip install '.[numpy,pytorch]'`.
- `array` is a nonempty writable 2D NumPy float32/64 array with positive strides, possibly noncontiguous. `tracked` is a nonempty 1D CPU tensor requiring gradients, possibly nonleaf, with finite float32/64 values.
- Return `(shared_tensor, logging_array)`. The tensor shares array storage with matching shape/dtype; later writes in either direction must propagate. The NumPy logging array holds the tracked values independently with its source shape and dtype, and is writable.
- Creating outputs leaves both sources' values and tracked history unchanged. Later changes to the tracked tensor or logging array must not affect the other.

A zero-copy conversion and an independent detached logging snapshot have different storage contracts.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/numpy-boundary
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.

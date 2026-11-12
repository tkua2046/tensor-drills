# Keep samples paired in ordered minibatches

PyTorch · Composite create

**Goal.** Produce ordered minibatches that keep each sample paired with its label.

Implement `labeled_batches(samples, labels, batch_size)` in [attempt.py](attempt.py).

- `samples` is a CPU float64 matrix `(N,D)` with `N>=0`, `D>=1`; labels is int64 `(N,)`. Values are finite. batch_size is a positive Python integer.
- Return a list of `(batch_samples, batch_labels)` pairs, each pair a tuple or list. Preserve order and pairing, include every sample exactly once, and keep a final partial batch. For N=0 return an empty list.
- Preserve both input values/dtypes and each batch's sample/label axes. Batch slices may alias inputs. Loops over batch boundaries are allowed.

For five samples and batch_size=2, return batch sizes 2, 2, and 1.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/labeled-batches
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.

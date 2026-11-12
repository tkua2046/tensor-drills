# Backpropagate a nonlinear scalar loss

PyTorch · Atomic create

**Goal.** Use backward() to compute the gradient of a nonlinear scalar objective on a trainable leaf.

Implement `scalar_gradient(values)` in [attempt.py](attempt.py).

- `values` is a nonempty 1D CPU float64 tensor, length at most 8, with finite entries in `[-3,3]` and `requires_grad=False`.
- Create an independent trainable leaf `x` with the same values, shape and dtype. Form scalar `loss = sum(x**3 + 2*x)`, call `backward()`, and return `(x, loss)`.
- Return the real loss tensor with its gradient history. `x.grad` must hold the gradient of that loss. Leave the supplied input unchanged, including gradient-tracking state.

For `[-2,0,1]`, the loss is `-9` and the leaf gradient is `[14,2,5]`.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/scalar-gradient
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.

# Place a model, inputs and new offsets together

PyTorch · Composite create

**Goal.** Run a supplied model on a requested device with inputs and intermediate tensors on a compatible device.

Implement `device_forward(model, features, device)` in [attempt.py](attempt.py).

- Features are a nonempty 2D CPU float32 tensor. The supplied float32 model starts on CPU and includes parameters and a registered buffer. The requested torch.device is CPU or an available CUDA/MPS device.
- Move the supplied model and features to the requested device. Create `offsets=arange(F)` in the feature dtype on that device, where F is the feature width. Return `(prediction, placed_features, offsets)` with `prediction=model(placed_features+offsets)`.
- Preserve feature values and dtype. CPU transfer may alias the input, but do not edit it. Moving the supplied model is intentional. Parameters, buffers and returned tensors must be compatible with the requested device.
- CPU is always checked. If no accelerator is available, the optional device case reports CPU rather than claiming accelerator coverage.

New tensors such as offsets need compatible placement as well as the model and inputs.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/device-forward
```

The untouched starter reports an unimplemented operation. For review, save your code and check output. Explain the actual tensor/module operations, state changes and evidence that meet the contract.

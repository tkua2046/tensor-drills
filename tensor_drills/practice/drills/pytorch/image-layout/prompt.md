# Convert flattened pixels to channel-first layout

PyTorch · Composite create

**Goal.** Convert pixels shaped (height * width, channels) to a batch of one in channel-first layout.

Implement `image_layout(x, height, width)` in [attempt.py](attempt.py).

The int64 pixel matrix is `(height*width,channels)`, ordered by row then column. Return `(1,channels,height,width)` with `out[0,c,h,w]=x[h*width+w,c]`. Height, width and channels are positive. Keep the batch axis even for one channel. Inputs may be noncontiguous; contiguous output is not required.

Use native operations without Python element or row loops. Preserve all input values, shapes and dtypes during the call. All tensors are on CPU and do not require gradients. Independent shape parameters are 1–8 unless another bound is stated; derived extents and selected counts follow their formulas.

Use [the Python setup](../../../README.md#setup) with PyTorch. Run from the drill workspace root.

```sh
tensor-drills check pytorch/image-layout
```

The untouched starter reports an unimplemented operation. Save your code and check output for review. Explain the operations, shapes and evidence that meet the contract.

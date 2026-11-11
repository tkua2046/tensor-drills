# Practice NumPy and PyTorch

Start with [NumPy row gathering](drills/numpy/row-gather/prompt.md) or [PyTorch row gathering](drills/pytorch/row-gather/prompt.md). Both tracks have drills on masks, matrix joining, indexing, reductions, independent slice repair, and indexed sums. PyTorch also has per-sequence broadcasting repair.

If arrays or tensors are new to you, try the [optional warm-up](#optional-warm-up) first.

Run `tensor-drills list --library numpy` or `tensor-drills list --library pytorch` from this workspace to see goals and prerequisites. Run `tensor-drills list --help` for all filters.

For training loop practice, see [PyTorch classifier debugging](drills/pytorch/classifier/prompt.md) and [PyTorch inline validation](drills/pytorch/inline-validation/prompt.md).

## Setup

Use the Python 3.12 or newer environment where you installed `tensor-drills`. Install NumPy or PyTorch in that environment if you did not include the corresponding package extra.

The bundled drills were verified on CPU with Python 3.12.4, NumPy 2.5.4, and PyTorch 2.15.0.

## Optional warm-up

Run the snippet for your track in the Python environment from Setup.

**NumPy**

```python
import numpy as np

values = np.array([[7, 8, 9], [10, 11, 12]], dtype=np.int64)
print(values.shape, values.dtype, values[1, 0])
```

**PyTorch**

```python
import torch

values = torch.tensor([[7, 8, 9], [10, 11, 12]], dtype=torch.int64)
print(values.shape, values.dtype, values[1, 0])
```

The shape is `(2, 3)`, so there are two rows and three columns. The dtype is `int64`. Indices start at zero, so `values[1, 0]` reads the second row and first column and gives `10`. Predict `values[0, 2]` and print it to check your answer.

## Run and submit

Open a prompt and edit its `attempt.py`, or copy the file elsewhere and pass the copy with `--attempt`. Run from this workspace directory.

```sh
tensor-drills check numpy/row-gather
tensor-drills check pytorch/row-gather
```

Run as often as you like. The checker reports each case and exits with `0` for a pass, `1` for an attempt failure, or `2` for a setup error. Each run has a 30-second limit.

To submit for review, save a copy of your attempt and run the same command with `--attempt path/to/saved_attempt.py`. Keep that copy, the drill ID, and the check output and exit status, including failures. Follow the prompt for any explanation to include. After the attempt, a person or an LLM can use `rubric.md` to review that evidence.

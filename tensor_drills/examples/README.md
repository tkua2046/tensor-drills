# NumPy and PyTorch interview drills

- [NumPy row gathering](drills/numpy/row-gather/prompt.md)
- [PyTorch classifier debugging](drills/pytorch/classifier/prompt.md)
- [PyTorch training with inline validation](drills/pytorch/inline-validation/prompt.md)

From this workspace, run `tensor-drills list` to see the drill goals and prerequisites. To narrow the list, try `tensor-drills list --library pytorch --topic autograd`. Run `tensor-drills list --help` for all filters.

## Setup

Use the Python 3.12 or newer environment where you installed `tensor-drills`. Install NumPy or PyTorch in that environment if you did not include the corresponding package extra.

The bundled drills were verified on CPU with Python 3.12.4, NumPy 2.5.4, and PyTorch 2.15.0.

## Run and submit

Open a prompt and edit its `attempt.py`, or copy the file elsewhere and pass the copy with `--attempt`. Run from this workspace directory.

```sh
tensor-drills check numpy/row-gather
tensor-drills check pytorch/classifier
tensor-drills check pytorch/inline-validation
```

Run as often as you like. The checker reports each case and exits with `0` for a pass, `1` for an attempt failure, or `2` for a setup error. Each run has a 30-second limit.

To submit for review, save a copy of your attempt and run the same command with `--attempt path/to/saved_attempt.py`. Keep that copy, the drill ID, and the check output and exit status, including failures. Follow the prompt for any explanation to include. After the attempt, a person or an LLM can use `rubric.md` to review that evidence.

# Tensor Drills

Learn NumPy and PyTorch through hands-on exercises. Practice writing and debugging code, from indexing arrays to fixing training loops. Each drill gives you a task and starter code. Run local tests for feedback as you work, then use the rubric to review your solution and reasoning.

## Try your first drill

Choose NumPy or PyTorch and use Python 3.12 or newer. From a checkout of this repository on macOS or Linux, install the extra for your track and create a practice workspace. The commands below use NumPy. For PyTorch, substitute `'.[pytorch]'` in the install command. Use `'.[numpy,pytorch]'` to practice both.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install '.[numpy]'
tensor-drills init ../tensor-drills-practice
cd ../tensor-drills-practice
```

Open the prompt in your practice workspace and run the check for your track.

| Track | Prompt in your workspace | Check |
| --- | --- | --- |
| NumPy | `drills/numpy/row-gather/prompt.md` | `tensor-drills check numpy/row-gather` |
| PyTorch | `drills/pytorch/row-gather/prompt.md` | `tensor-drills check pytorch/row-gather` |

The starter is unfinished, so this first check should fail. Edit `attempt.py` next to the prompt and rerun the check as you work. After your attempt, use `rubric.md` in the same folder to review your reasoning. If you want a person or an LLM to review it, share your code, check output, and any explanation the prompt asks for.

## Choose a drill

Both tracks offer core practice in shapes, indexing, masks, storage, dtypes, reductions, and matrix products. NumPy practice continues into stable numerics, grouped data, streaming calculations and linear systems. PyTorch practice continues into autograd, model state, training updates and attention.

If you already know how a PyTorch training loop works, try [classifier debugging](tensor_drills/practice/drills/pytorch/classifier/prompt.md) and [inline validation](tensor_drills/practice/drills/pytorch/inline-validation/prompt.md).

See the skill map for available drills and what to practice next. [Shared skills](docs/SKILL_MAP.md#shared-skills) · [NumPy skills](docs/SKILL_MAP.md#numpy) · [PyTorch skills](docs/SKILL_MAP.md#pytorch)

Run `tensor-drills list` in your practice workspace to compare goals, prerequisites, and workload. The catalog also shows which drills prepare you for others.

```sh
tensor-drills list --library pytorch --scope atomic --topic indexing
```

Once you choose a drill, open `drills/<drill-id>/prompt.md` and run `tensor-drills check <drill-id>`. Use `tensor-drills list --help` for more filters.

## Python API

The checker can also run against any workspace with the same drill layout. It prints per-case results and returns `0` for a pass, `1` for an attempt failure, or `2` for a setup error.

```python
from tensor_drills import check, init_workspace

workspace = init_workspace("api-practice")
status = check("numpy/row-gather", workspace=workspace)
```

The untouched NumPy starter returns status `1`. Pass `attempt=...` to check a saved file. Existing workspaces that contain a variant can run it with `variant=True` or the CLI flag `--variant`.

See the [documentation index](docs/README.md) for design and curriculum docs, the [drill authoring guide](docs/DRILL_AUTHORING.md) for contributing drills, and the [changelog](CHANGELOG.md) for release notes.

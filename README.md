# Tensor Drills

Tensor Drills runs fixed tests for NumPy and PyTorch interview exercises. It ships with row gathering, classifier debugging, and inline validation, each with a Markdown review rubric.

See the [changelog](CHANGELOG.md) for changes to the package.

## Install and run

From the project directory, activate a Python 3.12 or newer environment. Choose the `numpy` or `pytorch` extra for one drill bank, or install both as shown.

```sh
uv pip install '.[numpy,pytorch]'
tensor-drills init practice
cd practice
tensor-drills list
tensor-drills check numpy/row-gather
```

The same install works with `python -m pip install '.[numpy,pytorch]'`. The plain package has no numerical library dependencies. The `init` command copies the examples into a new directory so you can edit and keep attempts there. Open its README to choose a drill and see how to submit an attempt for review.

## Find a drill

Run `tensor-drills list` from the practice workspace root, or pass `--workspace path/to/practice`. It lists drills with a `metadata.json` file and shows their goals, topics, workloads, and prerequisites.

```sh
tensor-drills list --library numpy --scope atomic --task-type create
tensor-drills list --library pytorch --topic autograd --topic evaluation --workload 3
```

Filters combine. Repeat `--topic` to require every named topic. `--workload` matches an exact rating from 1 to 5. Once you choose a drill, open `drills/<drill-id>/prompt.md` in the workspace.

When a drill is linked as prerequisite practice, its entry also shows which drills it prepares you for.

## Python API

The checker can also run against any workspace with the same drill layout. It prints per-case results and returns `0` for a pass, `1` for an attempt failure, or `2` for a setup error.

```python
from tensor_drills import check, init_workspace

workspace = init_workspace("practice")
status = check("numpy/row-gather", workspace=workspace)
```

The untouched NumPy starter returns status `1`. Pass `attempt=...` to check a saved file. Existing workspaces that contain a variant can run it with `variant=True` or the CLI flag `--variant`.

For drill authoring, tests, and package builds, see [DEVNOTES.md](DEVNOTES.md).

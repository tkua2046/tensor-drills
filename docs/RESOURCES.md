# Resources and Drill Sources

This register records the public references used in the curriculum, exercise design, and technical checks. Each bundled drill supplies the material needed to attempt and check it. [Content design](CONTENT_DESIGN.md)

## Reviewed resources

| Resource | Reviewed location and date | Use in Tensor Drills |
| --- | --- | --- |
| [NumPy Quickstart](https://numpy.org/doc/stable/user/quickstart.html) and [NumPy Fundamentals](https://numpy.org/doc/stable/user/basics) | NumPy 2.5 manual, reviewed 2026-11-11 | Use shape, indexing, dtypes, broadcasting, and copies and views to establish the NumPy foundations. |
| [NumPy broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) | NumPy 2.5 manual, general broadcasting rules, reviewed 2026-11-11 | Verify axis alignment and singleton dimensions in expected behaviors. |
| [100 NumPy Exercises](https://github.com/rougier/numpy-100) | Repository overview and exercise catalog, reviewed 2026-11-11 | Reference for short exercises and for keeping hints and solutions separate from prompts. |
| [w3resource NumPy exercises](https://www.w3resource.com/python-exercises/numpy/index.php) | NumPy exercise index, reviewed 2026-11-11 | Reference for grouping practice by topic. |
| [PyTorch Learn the Basics](https://docs.pytorch.org/tutorials/beginner/basics/intro.html) | PyTorch tutorials, reviewed 2026-11-11 | Use the tensor, model, autograd, optimization, data, and persistence topics to check PyTorch coverage. |
| [PyTorch broadcasting semantics](https://docs.pytorch.org/docs/2.15/notes/broadcasting.html) and [Tensor Views](https://docs.pytorch.org/docs/2.15/tensor_view.html) | PyTorch 2.15 documentation, reviewed 2026-11-11 | Verify expected alignment, shared storage, and copying behavior. |
| [Learn PyTorch for Deep Learning](https://github.com/mrdbourke/pytorch-deep-learning) | [Tensor fundamentals exercises](https://www.learnpytorch.io/00_pytorch_fundamentals/#exercises) and [workflow exercises](https://www.learnpytorch.io/01_pytorch_workflow/#exercises), reviewed 2026-11-11 | Reference for giving tensor skills dedicated practice before applying them in model training. |
| [Tensor Puzzles](https://github.com/srush/Tensor-Puzzles) | Puzzle descriptions and [check implementation](https://github.com/srush/Tensor-Puzzles/blob/main/lib.py), reviewed 2026-11-11 | Reference for short shape-aware tasks and checking solutions against independently specified behavior. |
| [Udacity Deep Learning with PyTorch](https://github.com/udacity/deep-learning-v2-pytorch/blob/b85394e523e4b681c3bb55602e140319381b6698/intro-to-pytorch/README.md) | Intro lesson outline and exercise notebooks for tensors, networks, training, validation, and data loading at commit `b85394e`, reviewed 2026-11-11 | Reference for moving from tensors and matrix multiplication to models, backpropagation, training, and validation. [Repository license at the reviewed revision](https://github.com/udacity/deep-learning-v2-pytorch/blob/b85394e523e4b681c3bb55602e140319381b6698/LICENSE) |

## Drill source records

Link each drill record to its prompt when available. For each public source used, record what it contributed and what changed. Include applicable attribution and license notices. [How we choose drills](CONTENT_DESIGN.md#how-we-choose-drills)

| Origin | What to record |
| --- | --- |
| Original | Any references used to check behavior. Link to the [skill map](SKILL_MAP.md) or [content implementation plan](CONTENT_IMPLEMENTATION_PLAN.md) for the reason the task belongs in the catalog. |
| Inspired | The exact source section, the idea it contributed, and the task or checks designed for Tensor Drills. |
| Adapted | The exact source file and revision, the prompt, code, fixture, or other material carried over, and what changed. Record the applicable license and attribution, and include any required notices with the distributed material. |
| Unrecorded | The available history for a pre-existing drill when its origin cannot be established. |

### Bundled drills

| Drill | Origin | Source use |
| --- | --- | --- |
| [numpy/row-gather](../tensor_drills/practice/drills/numpy/row-gather/prompt.md) | Unrecorded | Project pilot. |
| [pytorch/classifier](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) | Unrecorded | Project pilot. |
| [pytorch/inline-validation](../tensor_drills/practice/drills/pytorch/inline-validation/prompt.md) | Unrecorded | Follow-up developed from the classifier pilot. |
| [`numpy/build-mask`](../tensor_drills/practice/drills/numpy/build-mask/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`numpy/stack-concat`](../tensor_drills/practice/drills/numpy/stack-concat/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`numpy/paired-cartesian`](../tensor_drills/practice/drills/numpy/paired-cartesian/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`numpy/reduce-axes`](../tensor_drills/practice/drills/numpy/reduce-axes/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#reductions-and-projection). |
| [`pytorch/build-mask`](../tensor_drills/practice/drills/pytorch/build-mask/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/stack-concat`](../tensor_drills/practice/drills/pytorch/stack-concat/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`pytorch/paired-cartesian`](../tensor_drills/practice/drills/pytorch/paired-cartesian/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/reduce-axes`](../tensor_drills/practice/drills/pytorch/reduce-axes/prompt.md) | Original | [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#reductions-and-projection). |
| [`pytorch/row-gather`](../tensor_drills/practice/drills/pytorch/row-gather/prompt.md) | Adapted | Uses the contract of the [NumPy row-gather drill](../tensor_drills/practice/drills/numpy/row-gather/prompt.md) from `v0.1.0`. The starter, fixtures, and checks use CPU tensors and require no NumPy installation. |

### Planned drills

| Drill | Origin | Source use |
| --- | --- | --- |
| `numpy/row-mean` | Original | NumPy Quickstart as a behavior reference for reductions. |
| `numpy/row-center` | Original | NumPy broadcasting rules as a behavior reference. |
| `pytorch/time-mean` | Original | The PyTorch Fundamentals exercises inform the position of reductions in the skill map. |
| `pytorch/sequence-offset` | Original | PyTorch broadcasting semantics as a behavior reference. |

Update the skill map and the drill source record in the same change as the drill. When revisiting a source, record the section or revision actually consulted. [Skill map](SKILL_MAP.md)

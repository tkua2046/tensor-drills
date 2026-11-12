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
| [`numpy/independent-slice`](../tensor_drills/practice/drills/numpy/independent-slice/prompt.md) | Original | New task and fixtures distinguish source preservation during an edit from independence under later writes. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`numpy/indexed-sum`](../tensor_drills/practice/drills/numpy/indexed-sum/prompt.md) | Original | New task and fixtures distinguish repeated-index accumulation, explicit output size, and dtype preservation. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/independent-slice`](../tensor_drills/practice/drills/pytorch/independent-slice/prompt.md) | Original | New task and fixtures distinguish source preservation during an edit from independence under later writes. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`pytorch/indexed-sum`](../tensor_drills/practice/drills/pytorch/indexed-sum/prompt.md) | Original | New task and fixtures distinguish repeated-index accumulation, explicit output size, and dtype preservation. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/sequence-offset`](../tensor_drills/practice/drills/pytorch/sequence-offset/prompt.md) | Original | New task and fixtures contrast unequal-axis errors with equal-axis misalignment. PyTorch broadcasting semantics remains a behavior reference in [reviewed resources](#reviewed-resources). [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-selection-and-broadcasting). |
| [`numpy/convert-dtype`](../tensor_drills/practice/drills/numpy/convert-dtype/prompt.md) | Original | Native casting, shape preservation, and stored-value semantics. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`numpy/split-sections`](../tensor_drills/practice/drills/numpy/split-sections/prompt.md) | Original | Unequal sections, zero-sized parts, and reconstruction. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`numpy/row-gather-many`](../tensor_drills/practice/drills/numpy/row-gather-many/prompt.md) | Original | Per-row rank-two indices, ordered repeats, and empty shapes. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`numpy/conditional-replace`](../tensor_drills/practice/drills/numpy/conditional-replace/prompt.md) | Original | Independent shape-preserving replacement, including no-op inputs. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`numpy/masked-assign`](../tensor_drills/practice/drills/numpy/masked-assign/prompt.md) | Original | Intentional mutation through aliases and noncontiguous views. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`numpy/shared-weight-matmul`](../tensor_drills/practice/drills/numpy/shared-weight-matmul/prompt.md) | Original | Shared feature contraction with batch-local results and numerical allowances. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#reductions-and-projection). |
| [`pytorch/convert-dtype`](../tensor_drills/practice/drills/pytorch/convert-dtype/prompt.md) | Original | Native casting, shape preservation, and stored-value semantics. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`pytorch/split-sections`](../tensor_drills/practice/drills/pytorch/split-sections/prompt.md) | Original | Unequal sections, zero-sized parts, and reconstruction. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#shapes-dtypes-and-storage). |
| [`pytorch/row-gather-many`](../tensor_drills/practice/drills/pytorch/row-gather-many/prompt.md) | Original | Per-row rank-two indices, ordered repeats, and empty shapes. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/conditional-replace`](../tensor_drills/practice/drills/pytorch/conditional-replace/prompt.md) | Original | Independent shape-preserving replacement, including no-op inputs. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/masked-assign`](../tensor_drills/practice/drills/pytorch/masked-assign/prompt.md) | Original | Intentional mutation through aliases and noncontiguous views. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#indexing-and-masks). |
| [`pytorch/shared-weight-matmul`](../tensor_drills/practice/drills/pytorch/shared-weight-matmul/prompt.md) | Original | Shared feature contraction with batch-local results and numerical allowances. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#reductions-and-projection). |
| [`numpy/row-mean`](../tensor_drills/practice/drills/numpy/row-mean/prompt.md) | Original | Axis repair with surviving row shape. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#numpy-reductions-and-broadcasting). NumPy Quickstart remains a behavior reference in [reviewed resources](#reviewed-resources). |
| [`pytorch/time-mean`](../tensor_drills/practice/drills/pytorch/time-mean/prompt.md) | Original | Time reduction with surviving batch and feature axes. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-selection-and-broadcasting). PyTorch tensor fundamentals remains a curriculum reference in [reviewed resources](#reviewed-resources). |
| [`numpy/row-softmax`](../tensor_drills/practice/drills/numpy/row-softmax/prompt.md) | Original | Stable per-row probabilities from elementary NumPy operations. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#row-normalization). |
| [`numpy/precise-sum`](../tensor_drills/practice/drills/numpy/precise-sum/prompt.md) | Original | Quantized readings expose precision lost before conversion. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#numpy-numerical-workflows). |
| [`numpy/safe-integer-sum`](../tensor_drills/practice/drills/numpy/safe-integer-sum/prompt.md) | Original | Bounded integer readings expose accumulator overflow. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#numpy-numerical-workflows). |
| [`numpy/seeded-sample`](../tensor_drills/practice/drills/numpy/seeded-sample/prompt.md) | Original | Caller-seeded local PCG64 choice and global-state preservation. [Curriculum rationale](CONTENT_IMPLEMENTATION_PLAN.md#numpy-numerical-workflows). |
| [`pytorch/classifier-forward`](../tensor_drills/practice/drills/pytorch/classifier-forward/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-data-and-model-state). |
| [`pytorch/scalar-gradient`](../tensor_drills/practice/drills/pytorch/scalar-gradient/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-gradients-and-training). |
| [`pytorch/gradient-sequence`](../tensor_drills/practice/drills/pytorch/gradient-sequence/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-gradients-and-training). |
| [`pytorch/detach-snapshots`](../tensor_drills/practice/drills/pytorch/detach-snapshots/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-graph-masking-and-routing). |
| [`pytorch/trainable-fork`](../tensor_drills/practice/drills/pytorch/trainable-fork/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-graph-masking-and-routing). |
| [`pytorch/mode-and-recording`](../tensor_drills/practice/drills/pytorch/mode-and-recording/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-gradients-and-training). |
| [`pytorch/train-step`](../tensor_drills/practice/drills/pytorch/train-step/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-gradients-and-training). |
| [`pytorch/device-forward`](../tensor_drills/practice/drills/pytorch/device-forward/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-gradients-and-training). |
| [`pytorch/numpy-boundary`](../tensor_drills/practice/drills/pytorch/numpy-boundary/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-conversion). |
| [`pytorch/labeled-batches`](../tensor_drills/practice/drills/pytorch/labeled-batches/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-data-and-model-state). |
| [`pytorch/model-roundtrip`](../tensor_drills/practice/drills/pytorch/model-roundtrip/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#pytorch-data-and-model-state). |
| [`pytorch/row-softmax`](../tensor_drills/practice/drills/pytorch/row-softmax/prompt.md) | Original | Self-contained native-operation and state evidence for the [planned outcome](CONTENT_IMPLEMENTATION_PLAN.md#row-normalization). |

### Planned drills

| Drill | Origin | Source use |
| --- | --- | --- |
| `numpy/row-center` | Original | NumPy broadcasting rules as a behavior reference. |

Update the skill map and the drill source record in the same change as the drill. When revisiting a source, record the section or revision actually consulted. [Skill map](SKILL_MAP.md)

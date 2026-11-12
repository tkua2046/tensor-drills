# NumPy and PyTorch Skill Map

Choose a track and find the skill you want to practice. Each topic lists the intended practice and links any bundled drills. Links marked “applied practice” cover the skill within a larger task. A dash means no bundled drill is linked for that outcome.

[Shared skills](#shared-skills) · [NumPy](#numpy) · [PyTorch](#pytorch)

Run `tensor-drills list --library numpy` or `tensor-drills list --library pytorch` in your practice workspace to see the drills you can run. See the implementation plan for the delivery order and each skill's scheduled or deferred coverage. [Setup and first drill](../README.md#try-your-first-drill) · [Delivery and coverage](CONTENT_IMPLEMENTATION_PLAN.md#skill-coverage)

## Shared skills

These skills apply to both libraries. Use the drill link for your track.

### Shared shapes, dtypes, and layout

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Allocation and dtype conversion | Allocate with a target shape and dtype. Cast existing values and check truncation. | Dtype conversion: [NumPy](../tensor_drills/practice/drills/numpy/convert-dtype/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/convert-dtype/prompt.md). General shape allocation remains deferred. |
| Reshape | Split an axis into heads and merge them while preserving value order. | [NumPy head reshape](../tensor_drills/practice/drills/numpy/head-reshape/prompt.md) · [PyTorch head reshape](../tensor_drills/practice/drills/pytorch/head-reshape/prompt.md) |
| Axis movement and insertion | Check positions after a permutation and preserve a singleton batch when squeezing. | [NumPy axis layout](../tensor_drills/practice/drills/numpy/axis-layout/prompt.md) · [PyTorch axis layout](../tensor_drills/practice/drills/pytorch/axis-layout/prompt.md) |
| Stacking and concatenation | Compare stacking on a new axis with concatenating along an existing axis. | [NumPy](../tensor_drills/practice/drills/numpy/stack-concat/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/stack-concat/prompt.md) |
| Splitting | Split unequal sections and join them in order. | [NumPy](../tensor_drills/practice/drills/numpy/split-sections/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/split-sections/prompt.md) |
| Slicing and storage | Create a stepped view and an independent copy. Diagnose unintended mutation through a view. | Independent result and alias diagnosis: [NumPy](../tensor_drills/practice/drills/numpy/independent-slice/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/independent-slice/prompt.md). Shared views: [NumPy shared slice](../tensor_drills/practice/drills/numpy/shared-slice/prompt.md) · [PyTorch shared slice](../tensor_drills/practice/drills/pytorch/shared-slice/prompt.md) |
| Image layout | Reshape and permute a non-square image to channel-first layout. | [NumPy image layout](../tensor_drills/practice/drills/numpy/image-layout/prompt.md) · [PyTorch image layout](../tensor_drills/practice/drills/pytorch/image-layout/prompt.md) |
| Noncontiguous layout | Flatten a transposed or stepped input in logical order and observe its storage relationship. | [NumPy flatten layout](../tensor_drills/practice/drills/numpy/flatten-layout/prompt.md) · [PyTorch flatten layout](../tensor_drills/practice/drills/pytorch/flatten-layout/prompt.md) |
| Expansion and copying | Compare a broadcast expansion with an independently writable copy. | [NumPy expand copy](../tensor_drills/practice/drills/numpy/expand-copy/prompt.md) · [PyTorch expand copy](../tensor_drills/practice/drills/pytorch/expand-copy/prompt.md) |

### Shared indexing and masks

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Gathering one value per row | Gather one value per row using its column index. | [NumPy](../tensor_drills/practice/drills/numpy/row-gather/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/row-gather/prompt.md) |
| Gathering several values per row | Gather several values per row using their column indices. | [NumPy](../tensor_drills/practice/drills/numpy/row-gather-many/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/row-gather-many/prompt.md) |
| Paired and Cartesian indexing | Select coordinate pairs and a grid of combinations. Preserve index order and repeats. | [NumPy](../tensor_drills/practice/drills/numpy/paired-cartesian/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/paired-cartesian/prompt.md) |
| Boolean masks | Combine bounds, invert a condition, and test values at each boundary. | [NumPy](../tensor_drills/practice/drills/numpy/build-mask/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/build-mask/prompt.md) |
| Boolean selection | Select individual elements or retain whole rows, including when no rows match. | [NumPy boolean select](../tensor_drills/practice/drills/numpy/boolean-select/prompt.md) · [PyTorch boolean select](../tensor_drills/practice/drills/pytorch/boolean-select/prompt.md) |
| Masked replacement and assignment | Compare a shape-preserving new result with assignment that intentionally mutates shared storage. | Replacement: [NumPy](../tensor_drills/practice/drills/numpy/conditional-replace/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/conditional-replace/prompt.md). Assignment: [NumPy](../tensor_drills/practice/drills/numpy/masked-assign/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/masked-assign/prompt.md). |
| Mask alignment | Apply each timestep flag across features without storing repeated masks. | [NumPy masked mean (applied practice)](../tensor_drills/practice/drills/numpy/masked-mean/prompt.md) · [PyTorch masked mean (applied practice)](../tensor_drills/practice/drills/pytorch/masked-mean/prompt.md) |
| Slicing and masks | Select valid rows from a slice using a mask aligned to the original input. | [NumPy window mask](../tensor_drills/practice/drills/numpy/window-mask/prompt.md) · [PyTorch window mask](../tensor_drills/practice/drills/pytorch/window-mask/prompt.md) |
| Repeated destinations | Sum all contributions at repeated indices and leave unused destinations at zero. | [NumPy](../tensor_drills/practice/drills/numpy/indexed-sum/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/indexed-sum/prompt.md) |
| Aligning values and indices | Pair row maxima with their indices and keep labels aligned through a top-k selection. | [NumPy row max](../tensor_drills/practice/drills/numpy/row-max/prompt.md) · [PyTorch row max](../tensor_drills/practice/drills/pytorch/row-max/prompt.md). Top-k label alignment remains planned. |
| Causal masking | Compare query and key positions, then combine the mask with padding. | [NumPy causal mask](../tensor_drills/practice/drills/numpy/causal-mask/prompt.md) · [PyTorch causal mask](../tensor_drills/practice/drills/pytorch/causal-mask/prompt.md) |

### Shared reductions, broadcasting, and products

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Single-axis reductions | Reduce one axis while preserving the others. | [NumPy row mean](../tensor_drills/practice/drills/numpy/row-mean/prompt.md) · [PyTorch time mean](../tensor_drills/practice/drills/pytorch/time-mean/prompt.md) |
| Multi-axis reductions | Reduce across several axes and retain dimensions so the result can broadcast when centering the input. | [NumPy](../tensor_drills/practice/drills/numpy/reduce-axes/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/reduce-axes/prompt.md) |
| Broadcasting | Align per-timestep or per-sequence operands with a batch of sequences. | Per-sequence offsets: [PyTorch](../tensor_drills/practice/drills/pytorch/sequence-offset/prompt.md) · [NumPy broadcast calibration](../tensor_drills/practice/drills/numpy/broadcast-calibration/prompt.md) · [PyTorch broadcast calibration](../tensor_drills/practice/drills/pytorch/broadcast-calibration/prompt.md) |
| Broadcasting in a calculation | Apply sample offsets and feature scales, or broadcast a computed row mean to center an array. | [NumPy row center](../tensor_drills/practice/drills/numpy/row-center/prompt.md) · [NumPy broadcast calibration](../tensor_drills/practice/drills/numpy/broadcast-calibration/prompt.md) · [PyTorch broadcast calibration](../tensor_drills/practice/drills/pytorch/broadcast-calibration/prompt.md) |
| Masked mean | Count valid timesteps and handle an all-invalid sequence. | [NumPy masked mean](../tensor_drills/practice/drills/numpy/masked-mean/prompt.md) · [PyTorch masked mean](../tensor_drills/practice/drills/pytorch/masked-mean/prompt.md) |
| Elementwise and matrix products | Compare the values of two products that have the same output shape. | [NumPy product kinds](../tensor_drills/practice/drills/numpy/product-kinds/prompt.md) · [PyTorch product kinds](../tensor_drills/practice/drills/pytorch/product-kinds/prompt.md) |
| Batched contraction | Apply shared weights to distinct batch items with rectangular inputs. | [NumPy](../tensor_drills/practice/drills/numpy/shared-weight-matmul/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/shared-weight-matmul/prompt.md) |
| Batched projection | Apply each batch item's own weight matrix to its masked mean. | [NumPy batched projection](../tensor_drills/practice/drills/numpy/batched-projection/prompt.md) · [PyTorch batched projection](../tensor_drills/practice/drills/pytorch/batched-projection/prompt.md) |

## NumPy

Start with the [shared skills](#shared-skills), then explore NumPy numerical work and data processing.

### NumPy numerical methods

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Accumulator dtype | Choose a dtype that avoids integer overflow or preserves small values in a sum. | [Precise floating sum](../tensor_drills/practice/drills/numpy/precise-sum/prompt.md) · [Safe integer sum](../tensor_drills/practice/drills/numpy/safe-integer-sum/prompt.md) |
| Stable probabilities | Compute row softmax with elementary operations and large logits. | [Row softmax](../tensor_drills/practice/drills/numpy/row-softmax/prompt.md) |
| Preprocessing and normalization | Standardize selected rows and compute a masked RMS normalization that handles empty rows and zero norms. | — |
| Stable masked calculations | Compute masked softmax with broadcast masks and wide half-precision inputs. Practice the distinct empty-row behavior of masked log-sum-exp. | — |
| Streaming numerics | Compute entropy with fixed-size state and check invariance to chunk boundaries. | — |

### NumPy sampling, selection, and grouping

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Reproducible sampling | Sample without replacement using a caller-provided seed and a local generator. | [Seeded sample](../tensor_drills/practice/drills/numpy/seeded-sample/prompt.md) |
| Target score gathering | Handle ignored targets even when the sentinel is a valid class index. | — |
| Masked ranking | Keep candidate IDs aligned and apply a deterministic rule for tied scores. | — |
| Sorted search and partition | Find insertion boundaries, count sorted events, and select values without fully sorting. | — |
| Windows and unique groups | Build moving sums and window views. Recover original rows from unique rows and inverse indices. | — |
| Group statistics and metrics | Use indexed sums and counts for group means and per-class accuracy. Handle discarded entries and missing groups. | — |
| Grouped extrema and probabilities | Distinguish absent groups from groups with negative infinity and normalize scores within groups. | — |

### NumPy sequence and pairwise calculations

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Padded sequence summaries | Join the mean of the valid prefix and its last timestep, including empty sequences. | — |
| Per-sequence token loss | Combine stable normalization and target gathering with a mean over each sequence's valid prefix. | — |
| Distances and nearest neighbors | Compute pairwise squared distances without storing differences for each feature of each pair. Select nearest rows and handle ties. | — |
| Solves and pairwise metrics | Work with different right-hand-side ranks, ridge regression, and pairwise cosine similarity. | — |
| Masked attention | Combine scaled scores, empty-query handling, and value weighting. | — |

## PyTorch

Start with the [shared skills](#shared-skills), then explore PyTorch autograd, model training, and model state.

### PyTorch tensor data and layout

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Device placement | Keep model parameters, inputs, and intermediates on compatible devices. | [Device forward](../tensor_drills/practice/drills/pytorch/device-forward/prompt.md) |
| NumPy conversion | Compare shared CPU storage with independent copies and capture a logging snapshot of a tensor that tracks gradients. | [NumPy boundary](../tensor_drills/practice/drills/pytorch/numpy-boundary/prompt.md) (requires both packages) |
| Batched gathering | Gather a class score per token and gather beam information on a middle axis. | — |
| Head layout and storage | Pack a sliced head tensor with a nonzero storage offset, explicit feature order, and contiguous output. | — |
| Routing and accumulation | Select a shortlist, keep features aligned with destinations, and sum repeated destinations within each batch. | — |

### PyTorch autograd and training

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Scalar backward | Compute the gradient of a scalar objective and inspect it on the input. | [Scalar gradient](../tensor_drills/practice/drills/pytorch/scalar-gradient/prompt.md) |
| Gradient accumulation | Isolate how gradients accumulate and clear across fresh forwards. | [Gradient sequence](../tensor_drills/practice/drills/pytorch/gradient-sequence/prompt.md) · [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) (applied practice) |
| Detach and storage | Produce both shared and independent detached tensors and observe the effects of mutation. | [Detach snapshots](../tensor_drills/practice/drills/pytorch/detach-snapshots/prompt.md) |
| Evaluation mode and gradient recording | Distinguish evaluation mode from disabled gradient recording and check both during evaluation. | [Mode and recording](../tensor_drills/practice/drills/pytorch/mode-and-recording/prompt.md) · [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) (applied practice) |
| Supervised updates | Write one training step from a stub and diagnose wrong loss inputs or update ordering in a repair task. | [Train step](../tensor_drills/practice/drills/pytorch/train-step/prompt.md) |
| Training and evaluation loops | Diagnose gradient carryover and active dropout during evaluation. Restore training behavior when validation runs between updates. | [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) · [Inline validation](../tensor_drills/practice/drills/pytorch/inline-validation/prompt.md) |
| Gradients and mutation | Create an independent trainable fork. Trace non-scalar backward, retained intermediate gradients, and mutations to tensors saved for backward. | Independent leaf: [Trainable fork](../tensor_drills/practice/drills/pytorch/trainable-fork/prompt.md). Saved-tensor mutation and non-scalar backward remain planned. |
| Manual and custom gradients | Derive matrix gradients, extend them to shared weights and bias across batches, and verify a custom backward numerically. | — |
| Microbatch updates | Weight the update by valid-token counts and check optimizer state when no tokens are valid. | — |

### PyTorch modules and model state

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Module construction | Register layers and produce class logits with the expected batch shape. | [Classifier forward](../tensor_drills/practice/drills/pytorch/classifier-forward/prompt.md) |
| Batching and persistence | Keep samples paired with labels in minibatches. Restore parameters and confirm predictions. | [Labeled batches](../tensor_drills/practice/drills/pytorch/labeled-batches/prompt.md) · [Model roundtrip](../tensor_drills/practice/drills/pytorch/model-roundtrip/prompt.md) |
| Parameters and buffers | Register trainable parameters, persistent buffers, and temporary buffers that follow module dtype and device. | — |

### PyTorch masking and sequence models

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Softmax | Normalize logits over the intended axis and check the probability values. | [Row softmax](../tensor_drills/practice/drills/pytorch/row-softmax/prompt.md) |
| Differentiable masking | Normalize over allowed positions and check gradients, including fully masked rows. Build a mask from key lengths. | — |
| Global valid-token loss | Check ignored gradients and the differentiable zero when every token is ignored. Practice shifting targets for next-token loss. | — |
| Rectangular causal attention | Use absolute positions, handle empty queries, and check outputs and gradients with independent fixtures. | — |
| Transformer debugging | Diagnose a causal masking bug using the invariant that later tokens cannot change earlier outputs. | — |

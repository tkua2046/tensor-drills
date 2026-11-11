# NumPy and PyTorch Skill Map

Choose a track and find the skill you want to practice. Each topic lists the intended practice and links any bundled drills. Links marked “applied practice” cover the skill within a larger task. A dash means no bundled drill is linked for that outcome.

[Shared skills](#shared-skills) · [NumPy](#numpy) · [PyTorch](#pytorch)

Run `tensor-drills list --library numpy` or `tensor-drills list --library pytorch` in your practice workspace to see the drills you can run. See the implementation plan for the delivery order. [Setup and first drill](../README.md#try-your-first-drill) · [Content implementation plan](CONTENT_IMPLEMENTATION_PLAN.md)

## Shared skills

These skills apply to both libraries. Use the drill link for your track.

### Shared shapes, dtypes, and layout

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Allocation and dtype conversion | Allocate with a target shape and dtype. Cast existing values and check truncation. | — |
| Reshape | Split an axis into heads and merge them while preserving value order. | — |
| Axis movement and insertion | Check positions after a permutation and preserve a singleton batch when squeezing. | — |
| Stacking and concatenation | Compare stacking on a new axis with concatenating along an existing axis. | [NumPy](../tensor_drills/practice/drills/numpy/stack-concat/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/stack-concat/prompt.md) |
| Splitting | Split unequal sections and join them in order. | — |
| Slicing and storage | Create a stepped view and an independent copy. Diagnose unintended mutation through a view. | — |
| Image layout | Reshape and permute a non-square image to channel-first layout. | — |
| Noncontiguous layout | Flatten a transposed or stepped input in logical order and observe its storage relationship. | — |
| Expansion and copying | Compare a broadcast expansion with an independently writable copy. | — |

### Shared indexing and masks

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Gathering one value per row | Gather one value per row using its column index. | [NumPy](../tensor_drills/practice/drills/numpy/row-gather/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/row-gather/prompt.md) |
| Gathering several values per row | Gather several values per row using their column indices. | — |
| Paired and Cartesian indexing | Select coordinate pairs and a grid of combinations. Preserve index order and repeats. | [NumPy](../tensor_drills/practice/drills/numpy/paired-cartesian/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/paired-cartesian/prompt.md) |
| Boolean masks | Combine bounds, invert a condition, and test values at each boundary. | [NumPy](../tensor_drills/practice/drills/numpy/build-mask/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/build-mask/prompt.md) |
| Boolean selection | Select individual elements or retain whole rows, including when no rows match. | — |
| Masked replacement and assignment | Compare a shape-preserving new result with assignment that intentionally mutates shared storage. | — |
| Mask alignment | Apply each timestep flag across features without storing repeated masks. | — |
| Slicing and masks | Select valid rows from a slice using a mask aligned to the original input. | — |
| Repeated destinations | Sum all contributions at repeated indices and leave unused destinations at zero. | — |
| Aligning values and indices | Pair row maxima with their indices and keep labels aligned through a top-k selection. | — |
| Causal masking | Compare query and key positions, then combine the mask with padding. | — |

### Shared reductions, broadcasting, and products

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Single-axis reductions | Reduce one axis while preserving the others. | — |
| Multi-axis reductions | Reduce across several axes and retain dimensions so the result can broadcast when centering the input. | [NumPy](../tensor_drills/practice/drills/numpy/reduce-axes/prompt.md) · [PyTorch](../tensor_drills/practice/drills/pytorch/reduce-axes/prompt.md) |
| Broadcasting | Align per-timestep or per-sequence operands with a batch of sequences. | — |
| Broadcasting in a calculation | Apply sample offsets and feature scales, or broadcast a computed row mean to center an array. | — |
| Masked mean | Count valid timesteps and handle an all-invalid sequence. | — |
| Elementwise and matrix products | Compare the values of two products that have the same output shape. | — |
| Batched contraction | Apply shared weights to distinct batch items with rectangular inputs. | — |
| Batched projection | Apply each batch item's own weight matrix to its masked mean. | — |

## NumPy

Start with the [shared skills](#shared-skills), then explore NumPy numerical work and data processing.

### NumPy numerical methods

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Accumulator dtype | Choose a dtype that avoids integer overflow or preserves small values in a sum. | — |
| Stable probabilities | Compute row softmax with elementary operations and large logits. | — |
| Preprocessing and normalization | Standardize selected rows and compute a masked RMS normalization that handles empty rows and zero norms. | — |
| Stable masked calculations | Compute masked softmax with broadcast masks and wide half-precision inputs. Practice the distinct empty-row behavior of masked log-sum-exp. | — |
| Streaming numerics | Compute entropy with fixed-size state and check invariance to chunk boundaries. | — |

### NumPy sampling, selection, and grouping

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Reproducible sampling | Sample without replacement using a caller-provided seed and a local generator. | — |
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
| Device placement | Keep model parameters, inputs, and intermediates on compatible devices. | — |
| NumPy conversion | Compare shared CPU storage with independent copies and capture a logging snapshot of a tensor that tracks gradients. | — |
| Batched gathering | Gather a class score per token and gather beam information on a middle axis. | — |
| Head layout and storage | Pack a sliced head tensor with a nonzero storage offset, explicit feature order, and contiguous output. | — |
| Routing and accumulation | Select a shortlist, keep features aligned with destinations, and sum repeated destinations within each batch. | — |

### PyTorch autograd and training

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Scalar backward | Compute the gradient of a scalar objective and inspect it on the input. | — |
| Gradient accumulation | Isolate how gradients accumulate and clear across fresh forwards. | [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) (applied practice) |
| Detach and storage | Produce both shared and independent detached tensors and observe the effects of mutation. | — |
| Evaluation mode and gradient recording | Distinguish evaluation mode from disabled gradient recording and check both during evaluation. | [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) (applied practice) |
| Supervised updates | Write one training step from a stub and diagnose wrong loss inputs or update ordering in a repair task. | — |
| Training and evaluation loops | Diagnose gradient carryover and active dropout during evaluation. Restore training behavior when validation runs between updates. | [Classifier debugging](../tensor_drills/practice/drills/pytorch/classifier/prompt.md) · [Inline validation](../tensor_drills/practice/drills/pytorch/inline-validation/prompt.md) |
| Gradients and mutation | Create an independent trainable fork. Trace non-scalar backward, retained intermediate gradients, and mutations to tensors saved for backward. | — |
| Manual and custom gradients | Derive matrix gradients, extend them to shared weights and bias across batches, and verify a custom backward numerically. | — |
| Microbatch updates | Weight the update by valid-token counts and check optimizer state when no tokens are valid. | — |

### PyTorch modules and model state

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Module construction | Register layers and produce class logits with the expected batch shape. | — |
| Batching and persistence | Keep samples paired with labels in minibatches. Restore parameters and confirm predictions. | — |
| Parameters and buffers | Register trainable parameters, persistent buffers, and temporary buffers that follow module dtype and device. | — |

### PyTorch masking and sequence models

| Skill | What to practice | Bundled drills |
| --- | --- | --- |
| Softmax | Normalize logits over the intended axis and check the probability values. | — |
| Differentiable masking | Normalize over allowed positions and check gradients, including fully masked rows. Build a mask from key lengths. | — |
| Global valid-token loss | Check ignored gradients and the differentiable zero when every token is ignored. Practice shifting targets for next-token loss. | — |
| Rectangular causal attention | Use absolute positions, handle empty queries, and check outputs and gradients with independent fixtures. | — |
| Transformer debugging | Diagnose a causal masking bug using the invariant that later tokens cannot change earlier outputs. | — |

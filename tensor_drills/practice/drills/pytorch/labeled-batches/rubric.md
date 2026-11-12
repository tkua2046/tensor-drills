# Keep samples paired in ordered minibatches rubric

## Ground truth

Ordered batching retains alignment and all samples, with a partial final batch and no empty batch for an empty dataset. Aliasing is permitted.

## Assessment

- Identifiable sample/label pairs catch independent ordering or dropped labels. Batch-size one, oversize and empty cases check boundary behavior.
- Accept native slicing, split operations with correct empty handling, or an ordered non-dropping DataLoader. Explain the paired batch boundaries.

[Fixed cases](tests.json)

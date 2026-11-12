# Gather several columns independently per row rubric

## Ground truth

Each output row uses its own index row. Selection order and repeated indices are retained, and shape is (N,K) even when either axis is zero. Values, dtype, and both inputs are preserved.

## Assessment

`different repeated columns` catches reusing one row's indices, sorting indices, or accidental Cartesian indexing. Empty row and selection axes and singleton cases retain (N,K). Inspect actual native gathering/indexing and aligned index shapes; equivalent advanced indexing or gather operations are valid.

Check the learner's code and explanation alongside the fixed-case output. A named API alone is insufficient evidence: identify the actual operands, shapes, and effects. Discuss avoidable allocations where useful while preserving equivalent valid approaches.

[Fixed cases](tests.json)

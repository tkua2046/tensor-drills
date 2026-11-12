# Compute signed pairwise cosine similarity rubric

## Ground truth

Norms reduce feature axes independently for each collection. Zero-vector handling is explicit; epsilon changes valid small-vector similarities.

## Assessment

Correctness: parallel/antiparallel/orthogonal, unequal scales, tiny nonzero and zero vectors, strided and empty collections. Inspect native contractions and norm axes.

Fixed cases: `signed cosine 0`, `signed cosine 1`, `signed cosine 2`, `signed cosine 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

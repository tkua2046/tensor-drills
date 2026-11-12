# Compose masked scaled attention rubric

## Ground truth

Scale uses key/query feature width, normalization uses the key axis, and values may have a different feature width. Empty rows need safe normalization.

## Assessment

Correctness: rectangular query/key and feature/value widths, broadcast masks, excluded scores, mixed fully masked queries, empty axes and strided inputs. Inspect contractions and normalization precision; a cast after float32 normalization is insufficient.

Fixed cases: `masked attention 0`, `masked attention 1`, `masked attention 2`, `masked attention 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

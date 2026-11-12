# Find nearest rows in bounded reference blocks rubric

## Ground truth

Each block contributes local minima, translated to global indices. A strict improvement retains the earlier reference on equal distance; running state stays query-sized.

## Assessment

Different block sizes, cross-block equal minima and the final partial block expose tie/offset/reset errors. Code and allocation reasoning assess the memory bound; fixed values alone cannot.

Fixed cases: `nearest block 1`, `nearest block 2`, `nearest block 3`, `nearest block 64`, `no queries`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

# Split and merge a feature axis rubric

## Ground truth

Splitting and merging retain logical feature order. Neither direction swaps the head and within-head coordinates.

## Assessment

Check each direction independently, including width64 from H=D=8, rather than accepting a round trip that could cancel two incorrect permutations. Inspect native shape operations and explain copying when needed.

Fixed case names: `split 2-3-2-3 contiguous`, `split 1-1-8-8 strided`, `split 1-2-1-3 contiguous`, `merge 2-3-2-3 transpose`, `merge 1-1-3-1 strided`, `merge 1-2-1-2 contiguous`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)

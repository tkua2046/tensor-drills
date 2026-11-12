# Align a window with full-input validity flags rubric

## Ground truth

The slice and validity flags refer to original row coordinates. Filtering first changes those coordinates.

## Assessment

Nonzero starts, stepped windows and valid rows outside the window distinguish filtering first or slicing flags inconsistently. Empty windows and no matches preserve the feature axis. Inspect native slice/mask alignment.

Fixed case names: `window 8-2-8-2 contiguous`, `window 5-1-4-1 strided`, `window 3-0-3-1 contiguous`, `window 4-2-2-1 contiguous`, `window 0-0-0-1 contiguous`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)

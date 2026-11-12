# Return a view and an independent slice rubric

## Ground truth

Basic slicing retains selected storage; copying separates it. Initial equality alone cannot establish either relationship.

## Assessment

Mutation probes test both sharing directions, unchanged unselected positions and isolation of the independent result. Inspect native slicing/copying and explain the difference from accidentally editing an aliased input.

Fixed case names: `slice 9-1-8-2 contiguous`, `slice 8-0-8-1 contiguous`, `slice 1-0-1-1 contiguous`, `slice 64-5-63-3 strided`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)

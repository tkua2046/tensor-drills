# Build broadcastable prefix key validity rubric

## Ground truth

Each length defines a half-open valid prefix; the singleton axes prepare the mask for head/query broadcasting.

## Assessment

Unsorted lengths and zero/full boundaries assess exact comparison and shape. Inspect native arange/broadcast construction.

Fixed cases: `key lengths 0`, `key lengths 1`, `key lengths 2`, `key lengths 3`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

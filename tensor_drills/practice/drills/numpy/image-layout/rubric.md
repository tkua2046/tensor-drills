# Convert flattened pixels to channel-first layout rubric

## Ground truth

Pixels first acquire spatial coordinates, then the channel axis moves ahead of them. The singleton batch remains explicit.

## Assessment

Non-square images and channel-specific values distinguish permutation from direct reshape. Inspect the native reshape and axis movement and explain one coordinate through the conversion.

Fixed case names: `image 2-3-3 contiguous`, `image 3-2-1 strided`, `image 1-4-2 contiguous`, `image 8-8-2 transpose`.

Use the saved code, check output and explanation as evidence. Required native operations and ownership explanations are assessed here in addition to fixed values. Equivalent approaches that meet the prompt are valid; general style suggestions are advisory.

[Fixed cases](tests.json)

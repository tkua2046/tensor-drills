# Pack head features into contiguous sequence order rubric

## Ground truth

Head/time coordinates must be permuted before combining head and feature dimensions; contiguity and gradient connectivity are separate requirements.

## Assessment

Logical-order, nonzero-offset and already-compatible layouts assess values, contiguity and source gradients. Inspect the actual permutation/packing and explain any necessary copy.

Fixed cases: `head packing 0`, `head packing 1`, `head packing 2`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

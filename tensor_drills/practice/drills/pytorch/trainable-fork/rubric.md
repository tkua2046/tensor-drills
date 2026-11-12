# Create an independent trainable fork rubric

## Ground truth

The fork owns its data and starts a fresh trainable graph. Copying without detaching can retain history; detaching without copying can retain storage.

## Assessment

- Nonleaf and strided sources separate history from data. A backward probe and mutation verify both kinds of independence.
- Inspect actual leaf construction; accept equivalent combinations of copy, detach and enabling gradients.

[Fixed cases](tests.json)

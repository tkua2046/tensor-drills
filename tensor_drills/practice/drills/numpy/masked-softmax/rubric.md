# Normalize allowed logits in float32 rubric

## Ground truth

Allowed logits determine the normalization. Low-precision accumulation can overflow even after max shifting; fully excluded rows need safe max/division paths.

## Assessment

The wide half rows separate accumulator overflow from exponential overflow. Mixed all-invalid rows and broadcast masks check semantics. Inspect promotion and safe intermediate calculations, not just final dtype.

Fixed cases: `masked probabilities float32`, `masked probabilities float16`, `wide half row 65536`, `wide half row 131072`.

Use saved code, output and reasoning as evidence. Native operation and allocation requirements need code inspection in addition to fixed values. Accept equivalent correct approaches; general style suggestions are advisory.

[Fixed cases](tests.json)

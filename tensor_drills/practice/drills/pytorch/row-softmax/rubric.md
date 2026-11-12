# Normalize each row with stable softmax rubric

## Ground truth

Stable normalization is row-local. Native softmax or a suitable per-row shifted calculation avoids overflow and preserves negligible tails under the stated allowance.

## Assessment

- Extreme positive and negative rows together expose global shifting. Exact probabilities catch wrong axes/global normalization beyond row-sum checks. Singleton/empty shapes preserve axes and dtype.
- Inspect actual vectorized Torch operations and the learner's axis explanation. Accept softmax and equivalent stable calculations; row loops miss the disclosed requirement.

[Fixed cases](tests.json)

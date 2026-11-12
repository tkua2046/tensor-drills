# Normalize each row with stable softmax rubric

## Ground truth

Normalization is independent for each row. A stable equivalent calculation shifts by a suitable row-local constant before exponentiation. Large common offsets must not cause overflow; negligible tails may underflow.

## Assessment

- Inspect actual elementary NumPy operations and row-local axes. Accept equivalent stable calculations and accumulator choices that preserve the return dtype.
- `large row offsets` catches unshifted exponentials and global normalization; `different rows` catches the wrong axis. Singleton/empty axes preserve shape. `subnormal probabilities` admits native exponential rounding near underflow.
- Compare probabilities, not just row sums. A Python loop or a delegated softmax helper can pass values but misses the disclosed operation requirement.

[Fixed cases](tests.json)

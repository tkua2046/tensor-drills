# Accumulate int32 readings without overflow rubric

## Ground truth

The reduction must avoid int32 wraparound before returning an int64 scalar. The length bound guarantees an exact int64 result. Default NumPy promotion is valid when it provides the required behavior.

## Assessment

- Positive and negative overflow cases expose int32 accumulation; casting after overflow does not repair the total. `maximum count` exercises the length bound.
- Inspect actual NumPy accumulation/promotion. Accept explicit accumulator dtype, widening before reduction, or a default reduction that satisfies the contract.
- Python element loops can compute correct totals but miss the stated native-operation requirement.

[Fixed cases](tests.json)

# Build and invert a Boolean mask rubric

## Ground truth

Inside is true for the half-open interval `[lower, upper)`. Outside flips every flag, including at the endpoints. Equal bounds produce an all-false inside mask. Both outputs have Boolean dtype and the input shape. The input stays unchanged.

## Assessment

- Use `both endpoints` to distinguish the inclusive lower bound and exclusive upper bound. `equal bounds` checks that the interval is empty even when an input equals the bound.
- Use `fractional matrix` to check both dimensions. `integer values with fractional bounds` detects truncating the bounds to the input dtype. The verifier checks both masks, Boolean dtype, and unchanged input in each case.
- Check that the learner explains why the lower endpoint is inside when the bounds differ and why the upper endpoint is always outside.

[Fixed cases](tests.json)

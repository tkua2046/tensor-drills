# Reduce across axes and center the input rubric

## Ground truth

For a fixed middle-axis position, sum and average over all `B * C` elements at that position. Totals drop both reduced axes, while means retain both as length-one axes. The mean for that position is subtracted from all its elements in the original shape. Preserve dtype and input values.

## Assessment

- Use `three distinct axes` to check the axis choice, sum versus mean, and centering each middle-axis position separately.
- Use `one middle position` to check the shape of the totals when `R = 1` and the tolerance for fractional means. `singleton reduced axes` checks that shape does not depend on which axes happen to have length one.
- Check that the code reduces with PyTorch operations and centers by broadcasting the mean across the input. Accept sequential reductions and equivalent ways of retaining or restoring length-one axes.
- Check that the learner identifies the operations and reduction axes in their code and explains how the actual subtraction operands align to keep a distinct mean for each middle-axis position.

[Fixed cases](tests.json)

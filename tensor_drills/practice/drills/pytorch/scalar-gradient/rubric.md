# Backpropagate a nonlinear scalar loss rubric

## Ground truth

The derivative is 3*x²+2, accumulated in the actual leaf .grad after backward. A copied leaf separates trainable state from the supplied values.

## Assessment

- Signed, zero and fractional entries check loss and derivative, actual .grad, leaf/history properties and independent storage.
- Inspect the actual backward call and loss construction. Manually assigning the analytic gradient can pass values but misses the explicit backward requirement. Accept equivalent independent-leaf construction.

[Fixed cases](tests.json)

# Share a NumPy input and freeze a logging snapshot rubric

## Ground truth

A CPU zero-copy conversion preserves ndarray storage, including positive-stride views. A logging snapshot must detach graph history and own data; detach alone still shares storage.

## Assessment

- Mutation in both directions proves sharing. Strided input and nonleaf tracking distinguish copy/history mistakes. Logging writes and source writes must remain isolated.
- Inspect actual conversion, detach and copy operations. Accept from_numpy or sharing as_tensor for the input, and equivalent detached-copy orders for logging. Both dependencies are intrinsic to this boundary exercise.

[Fixed cases](tests.json)

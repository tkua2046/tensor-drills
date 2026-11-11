# Compare paired and Cartesian indexing rubric

## Ground truth

The paired result contains one value per index position. The grid takes every listed row against every listed column. In particular, the paired result is the grid's diagonal. Both preserve the supplied order, repeats, and matrix dtype. The results keep shapes `(K,)` and `(K, K)` even for `K = 1`. All inputs stay unchanged.

## Assessment

- Use `unsorted repeated indices` to check order and repeats on both axes. The asymmetric values also expose a transposed grid. Use `rectangular matrix` to check distinct rows and columns with different axis sizes.
- Use `one index pair` to check that neither result loses a dimension. The verifier checks dtype and unchanged inputs in each case.
- Check the code for NumPy array indexing operations that take the supplied index arrays or indices derived from them. Accept equivalent approaches, such as chaining indexing operations or aligning index shapes for broadcasting.
- Check that the learner identifies the actual operations and index shapes in their code and explains which indices advance together and which vary independently.

[Fixed cases](tests.json)

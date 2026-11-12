# Separate gradient history from storage sharing rubric

## Ground truth

detach separates graph history but retains storage. An independent detached snapshot also needs its own data. Source history remains intact during creation.

## Assessment

- Leaf, nonleaf and strided cases prove storage relationships through writes, not pointer equality.
- Inspect actual detach/copy operations and explain why detach or contiguous alone does not guarantee independence. Accept clone-then-detach or detach-then-clone for the independent output.

[Fixed cases](tests.json)

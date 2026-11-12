# Repair one mean per row rubric

## Ground truth

Return one mean per row of a 2D array. The reduction divides the sum by the length of the named axis and preserves the input dtype and surviving axes. The input stays unchanged. Per-output error allowances admit ordinary native reduction rounding under the bounded reduction length.

## Assessment

The starter reduces rows instead of columns. `rectangular rows` exposes the wrong axis through shape; the square case exposes it through values. One-row, one-column, empty-row, and strided cases preserve the surviving axis. Inspect the selected axis and averaging denominator. Accept mean or an equivalent vectorized sum/division; do not require a named mean API.

Review code and explanation alongside the fixed-case output. A Python element-loop solution can pass values but misses the stated vectorization requirement.

[Fixed cases](tests.json)

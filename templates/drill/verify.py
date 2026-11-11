def check_case(call, inputs, expected):
    # Construct the declared input types and call the learner's function.
    result = call("solve", inputs["values"])

    # This sample checks a scalar. Use array or tensor assertions as needed.
    assert result == expected, f"Expected {expected!r}, got {result!r}."

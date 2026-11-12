import numpy as np


def assert_draw(actual, data, rows, count):
    assert isinstance(actual, np.ndarray), "Return a NumPy array."
    assert actual.shape == (count,), "Preserve the requested draw shape."
    assert actual.dtype == np.dtype("int64"), "Return int64 indices."
    assert np.unique(actual).size == count, "Sample without replacement."
    assert ((actual >= 0) & (actual < rows)).all(), "Return valid row indices."
    np.testing.assert_array_equal(actual, np.array(data, dtype=np.int64))


def check_case(call, inputs, expected):
    def invoke(seed, data):
        incoming = np.random.get_state()
        try:
            np.random.seed(913)
            before = np.random.get_state()
            result = call("seeded_sample", inputs["rows"], inputs["count"], seed)
            after = np.random.get_state()
            assert before[0] == after[0] and np.array_equal(before[1], after[1]) and before[2:] == after[2:], "Legacy global RNG state changed."
            assert_draw(result, data, inputs["rows"], inputs["count"])
        finally:
            np.random.set_state(incoming)
    invoke(inputs["seed"], expected["samples"])
    invoke(inputs["other_seed"], expected["other"])
    invoke(inputs["seed"], expected["samples"])

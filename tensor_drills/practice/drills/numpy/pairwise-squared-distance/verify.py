import numpy as np

def make(spec):
    result = np.full(spec["shape"], spec["fill"], dtype=spec["dtype"]) if "fill" in spec else np.array(spec["data"], dtype=spec["dtype"]).reshape(spec["shape"])
    if spec.get("layout") == "strided" and result.shape[-1]:
        shape = result.shape[:-1] + (2 * result.shape[-1] + 2,)
        backing = np.zeros(shape, dtype=result.dtype)
        view = backing[..., 1:1 + 2 * result.shape[-1]:2]
        view[...] = result
        return view
    if spec.get("layout") == "transpose" and result.ndim >= 2:
        return result.swapaxes(0, 1).copy().swapaxes(0, 1)
    return result

def same(actual, spec, label, index=False):
    assert isinstance(actual, np.ndarray), f"{label}: return a NumPy array."
    wanted = make(spec)
    assert actual.shape == wanted.shape, f"{label}: expected shape {wanted.shape}, got {actual.shape}."
    if index:
        assert np.issubdtype(actual.dtype, np.integer), f"{label}: use integer indices."
    else:
        assert actual.dtype == wanted.dtype, f"{label}: preserve the required dtype."
    if wanted.dtype.kind == "f":
        assert np.isfinite(actual).all(), f"{label}: require finite results."
        np.testing.assert_allclose(actual, wanted, rtol=1e-5 if wanted.dtype == np.float32 else 1e-10, atol=1e-7 if wanted.dtype == np.float32 else 1e-10, err_msg=label)
    else:
        np.testing.assert_array_equal(actual, wanted, err_msg=label)

def copy(value):
    return value.copy()

def unchanged(args, saved):
    for key, original in saved.items():
        actual = args[key]
        assert actual.shape == original.shape and actual.dtype == original.dtype, f"Input {key} metadata changed."
        np.testing.assert_array_equal(actual, original, err_msg=f"Input {key} changed")

def pair(value):
    assert isinstance(value, (tuple, list)) and len(value) == 2, "Return the two requested results."
    return value


def items(value, count):
    assert isinstance(value, (tuple, list)) and len(value) == count, f"Return {count} requested outputs."
    return value



def check_case(call, inputs, expected):
    import warnings
    args = {key: make(value) if isinstance(value, dict) and "shape" in value and "dtype" in value else value for key,value in inputs.items()}
    saved = {key: copy(value) for key,value in args.items() if isinstance(inputs[key],dict) and "shape" in inputs[key] and "dtype" in inputs[key]}
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        result=call("pairwise_squared_distance",args["x"],args["y"])
        same(result,expected,"Squared distances")
        assert bool((result>=0).all()), "Squared distances must be nonnegative."
    assert not caught, "The operation must emit no warnings."
    unchanged(args,saved)

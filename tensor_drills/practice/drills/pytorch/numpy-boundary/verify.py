import torch
from torch import nn


def tensor(data, shape=None, dtype=torch.float64):
    result = torch.tensor(data, dtype=dtype, device="cpu")
    return result.reshape(shape) if shape is not None else result


def same(actual, wanted, name):
    assert isinstance(actual, torch.Tensor), f"{name}: return a tensor."
    torch.testing.assert_close(actual, wanted, rtol=1e-8, atol=1e-10, msg=lambda m: f"{name}: {m}")


def tracked(inputs):
    base = tensor(inputs["values"]).requires_grad_()
    if inputs.get("strided"):
        base = base.repeat_interleave(2).detach().requires_grad_()
        source = base[::2]
    else:
        source = base * 1.0 if inputs.get("nonleaf") else base
    return base, source


import numpy as np


def check_case(call, inputs, expected):
    dtype=np.dtype(inputs["dtype"]);raw=np.array(inputs["array"],dtype=dtype)
    if inputs.get("strided"):
        base_array=np.zeros((raw.shape[0],2*raw.shape[1]),dtype=dtype);array=base_array[:,::2];array[:]=raw
    else:array=raw
    base=tensor(inputs["values"],dtype=getattr(torch, inputs.get("tracked_dtype", inputs["dtype"]))).requires_grad_();source=base*1.0 if inputs.get("nonleaf") else base
    original=source.detach().clone();history=source.grad_fn;array_copy=array.copy()
    result=call("numpy_boundary",array,source)
    assert isinstance(result,tuple) and len(result)==2,"Return (shared_tensor, logging_array)."
    shared,logging=result
    same(shared,torch.from_numpy(array_copy),"Shared values")
    assert isinstance(logging,np.ndarray) and logging.dtype==original.numpy().dtype and logging.shape==tuple(source.shape),"Return a matching NumPy logging array."
    np.testing.assert_array_equal(logging,original.numpy())
    assert source.requires_grad and source.grad_fn is history,"Source history changed."
    same(source,original,"Tracked source changed");np.testing.assert_array_equal(array,array_copy)
    array[:]=17;same(shared,torch.full_like(shared,17),"Array writes do not reach tensor")
    shared.fill_(-19);np.testing.assert_array_equal(array,np.full_like(array,-19))
    np.testing.assert_array_equal(logging,original.numpy())
    with torch.no_grad():source.fill_(23)
    np.testing.assert_array_equal(logging,original.numpy())
    logging[:]=-29;same(source,torch.full_like(source,23),"Logging write reaches source")

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


class DeviceModel(nn.Module):
    def __init__(self, inputs):
        super().__init__();self.linear=nn.Linear(len(inputs["scale"]),2,dtype=torch.float32)
        self.register_buffer("scale",tensor(inputs["scale"],dtype=torch.float32))
        with torch.no_grad():
            self.linear.weight.copy_(tensor(inputs["weight"],dtype=torch.float32));self.linear.bias.copy_(tensor(inputs["bias"],dtype=torch.float32))
    def forward(self,x):return self.linear(x*self.scale)


def check_case(call, inputs, expected):
    if inputs["device"]=="available":
        device=torch.device("cuda:0" if torch.cuda.is_available() else "mps" if torch.backends.mps.is_available() else "cpu")
    else:device=torch.device("cpu")
    print(f"Device exercised: {device}")
    model=DeviceModel(inputs);saved={k:v.clone() for k,v in model.state_dict().items()};features=tensor(inputs["values"],dtype=torch.float32);original=features.clone()
    result=call("device_forward",model,features,device)
    assert isinstance(result,tuple) and len(result)==3,"Return (prediction, placed_features, offsets)."
    prediction,placed,offsets=result
    for value in list(result)+list(model.parameters())+list(model.buffers()):
        assert isinstance(value,torch.Tensor) and value.device.type==device.type,"Keep all tensors and model state on the requested device."
        assert value.dtype==torch.float32,"Preserve float32 dtype."
    torch.testing.assert_close(prediction.cpu(),tensor(expected,dtype=torch.float32),rtol=1e-5,atol=1e-6)
    same(placed.cpu(),original,"Placed values");same(offsets.cpu(),torch.arange(features.shape[1],dtype=torch.float32),"Offsets")
    same(features,original,"Caller features changed")
    for k,v in model.state_dict().items():same(v.cpu(),saved[k],"Model values changed")

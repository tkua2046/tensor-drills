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


import tempfile
from pathlib import Path


class StatefulModel(nn.Module):
    def __init__(self):
        super().__init__();self.linear=nn.Linear(2,2,dtype=torch.float64);self.register_buffer("offset",torch.zeros(2,dtype=torch.float64))
    def forward(self,x):return self.linear(x)+self.offset


def check_case(call, inputs, expected):
    source=StatefulModel();destination=StatefulModel()
    with torch.no_grad():
        source.linear.weight.copy_(tensor(inputs["weight"]));source.linear.bias.copy_(tensor(inputs["bias"]));source.offset.copy_(tensor(inputs["offset"]))
        for p in destination.parameters():p.fill_(13)
        destination.offset.fill_(19)
    source.train(inputs["training"]);destination.train(not inputs["training"]);saved={k:v.clone() for k,v in source.state_dict().items()}
    with tempfile.TemporaryDirectory() as tmp:
        path=Path(tmp)/"state.pt";result=call("model_roundtrip",source,destination,path)
        assert result is destination,"Restore and return the supplied destination."
        assert path.is_file(),"Write the source state file."
        try:disk=torch.load(path,map_location="cpu",weights_only=True)
        except Exception as error:raise AssertionError(f"Loadable state file required: {error}") from error
        assert isinstance(disk,dict) and set(disk)==set(saved),"Save the bare state_dict, including its persistent buffer."
        for key,value in saved.items():
            same(disk[key],value,"Saved state");same(source.state_dict()[key],value,"Source changed");same(destination.state_dict()[key],value,"Restored state")
        assert source.training==inputs["training"] and destination.training!=inputs["training"],"Preserve both mode flags."
        same(destination(tensor(inputs["values"])),tensor(expected),"Restored prediction")
        with torch.no_grad():
            for p in source.parameters():p.add_(1)
            source.offset.add_(1)
        for key,value in saved.items():same(destination.state_dict()[key],value,"Destination aliases source state")

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


class CountedLoss(nn.CrossEntropyLoss):
    def __init__(self):
        super().__init__(reduction="mean"); self.calls=0
    def forward(self, scores, labels):
        self.calls+=1
        return super().forward(scores,labels)


def check_case(call, inputs, expected):
    model=nn.Linear(2,2,dtype=torch.float64)
    with torch.no_grad():
        model.weight.copy_(tensor(inputs["weight"]));model.bias.copy_(tensor(inputs["bias"]))
    model.eval();optimizer=torch.optim.SGD(model.parameters(),lr=inputs["lr"]);loss_fn=CountedLoss();forwards=[];steps=[]
    model.register_forward_pre_hook(lambda m,a:forwards.append([m.training,torch.is_grad_enabled()]))
    optimizer.register_step_pre_hook(lambda o,a,k:steps.append((None if model.weight.grad is None else model.weight.grad.clone(),None if model.bias.grad is None else model.bias.grad.clone())))
    for p in model.parameters():p.grad=torch.full_like(p,7)
    for index,(batch,wanted) in enumerate(zip(inputs["batches"],expected),1):
        features=tensor(batch["features"]);labels=tensor(batch["labels"],dtype=torch.int64);fx=features.clone();ly=labels.clone()
        result=call("train_step",model,loss_fn,optimizer,features,labels)
        assert len(forwards)==index and len(steps)==index and loss_fn.calls==index, "Use one supplied forward, loss and optimizer step per batch."
        assert forwards[-1]==[True,True] and model.training, "Train with recording enabled."
        same(result,tensor(wanted["loss"]),"Detached loss")
        assert not result.requires_grad and result.grad_fn is None,"Detach the returned loss."
        same(steps[-1][0],tensor(wanted["grad_w"]),"Gradients at step");same(steps[-1][1],tensor(wanted["grad_b"]),"Bias gradients at step")
        same(model.weight,tensor(wanted["weight"]),"Updated weights");same(model.bias,tensor(wanted["bias"]),"Updated bias")
        same(features,fx,"Features changed");same(labels,ly,"Labels changed")

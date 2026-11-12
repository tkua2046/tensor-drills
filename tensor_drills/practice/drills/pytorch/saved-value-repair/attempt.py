import torch
from torch import nn
from torch.nn import functional as F

def saved_value_repair(x):
    loss=(x*x).sum()
    updated=x.detach()
    updated.add_(1)
    loss.backward()
    return updated,loss

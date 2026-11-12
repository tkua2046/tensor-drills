import torch
from torch import nn
from torch.nn import functional as F

def microbatch_step(model, optimizer, batches):
    raise NotImplementedError

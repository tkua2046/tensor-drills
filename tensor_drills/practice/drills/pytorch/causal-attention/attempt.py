import torch
from torch import nn
from torch.nn import functional as F

def causal_attention(q, k, v, qpos, kpos, qvalid, kvalid):
    raise NotImplementedError

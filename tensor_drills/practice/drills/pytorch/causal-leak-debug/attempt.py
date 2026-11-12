import torch
from torch import nn
from torch.nn import functional as F

def causal_leak_debug(q, k, v, qpos, kpos, qvalid, kvalid):
    b,h,queries,dim=q.shape
    if q.shape[-2]==0 or k.shape[-2]==0:
        return (q.sum()+k.sum()+v.sum())*0+q.new_zeros((b,h,queries,v.shape[-1]))
    allowed=qvalid[:,None,:,None]&kvalid[:,None,None,:]
    scores=q@k.transpose(-1,-2)/(dim**.5)
    masked=scores.masked_fill(~allowed,-torch.inf)
    maximum=masked.amax(dim=-1,keepdim=True)
    safe=torch.where(torch.isfinite(maximum),maximum,0.)
    e=torch.exp(masked-safe)
    total=e.sum(dim=-1,keepdim=True)
    prob=e/torch.where(total>0,total,1.)
    return prob@v

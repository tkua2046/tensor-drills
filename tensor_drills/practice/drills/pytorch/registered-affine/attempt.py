import torch
from torch import nn
from torch.nn import functional as F

class RegisteredAffine:
    def __init__(self, *args):
        raise NotImplementedError

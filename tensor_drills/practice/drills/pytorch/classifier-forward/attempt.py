import torch
from torch import nn

class Classifier(nn.Module):
    def __init__(self, in_features, hidden_features, classes):
        super().__init__()
        raise NotImplementedError

    def forward(self, features):
        raise NotImplementedError

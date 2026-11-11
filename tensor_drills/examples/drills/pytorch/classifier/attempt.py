import torch
from torch.nn import functional as F


def train_step(model, optimizer, features, labels):
    model.train()
    loss = F.cross_entropy(model(features), labels)
    loss.backward()
    optimizer.step()


def evaluate(model, features):
    with torch.no_grad():
        return model(features)

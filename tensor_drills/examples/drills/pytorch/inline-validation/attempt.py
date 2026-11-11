import torch
from torch.nn import functional as F


def train_with_validation(model, optimizer, batches, validation_features):
    predictions = []
    model.train()
    for features, labels in batches:
        loss = F.cross_entropy(model(features), labels)
        loss.backward()
        optimizer.step()

        model.eval()
        with torch.no_grad():
            predictions.append(model(validation_features))
    return predictions

import torch


def build_masks(values: torch.Tensor, lower: int | float, upper: int | float) -> tuple[torch.Tensor, torch.Tensor]:
    raise NotImplementedError

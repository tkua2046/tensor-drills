import torch


def select_entries(
    matrix: torch.Tensor, rows: torch.Tensor, columns: torch.Tensor
) -> tuple[torch.Tensor, torch.Tensor]:
    raise NotImplementedError

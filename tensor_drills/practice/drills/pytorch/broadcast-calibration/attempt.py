import torch

def broadcast_calibration(x, offsets, bias, scale):
    return (x + offsets[:,None,:] + bias[:,None,None]) * scale

import numpy as np


def edit_slice(values, start, stop, step, increment):
    selected = values[start:stop:step]
    selected += increment
    return selected

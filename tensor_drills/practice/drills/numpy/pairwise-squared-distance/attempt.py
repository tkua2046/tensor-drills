import numpy as np

def pairwise_squared_distance(x, y):
    distance=(x*x).sum(axis=0)[:,None]+(y*y).sum(axis=0)[None,:]-2*(x@y.T)
    return np.maximum(distance,0)

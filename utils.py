import numpy as np
import matplotlib.pyplot as plt

def ray_tracing_numpy(x,y,poly):
    n = len(poly)
    inside = np.zeros(len(x),np.bool_)
    p2x = 0.0
    p2y = 0.0
    xints = 0.0
    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        idx = np.nonzero((y > min(p1y,p2y)) & (y <= max(p1y,p2y)) & (x <= max(p1x,p2x)))[0]
        if p1y != p2y:
            xints = (y[idx]-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
        if p1x == p2x:
            inside[idx] = ~inside[idx]
        else:
            idxx = idx[x[idx] <= xints]
            inside[idxx] = ~inside[idxx]

        p1x,p1y = p2x,p2y
    return inside

def plot(x,y):
    plt.scatter(x, y)
    plt.xlim([0, 600])
    plt.ylim([0, 400])
    plt.xticks(np.arange(0, 600 + 1, 50))
    plt.yticks(np.arange(0, 400 + 1, 50))
    plt.grid()
    plt.show()
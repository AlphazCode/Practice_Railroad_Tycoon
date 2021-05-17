import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from operator import itemgetter


def plot(x, y, square, lines):
    """
    Function to draw all points, most populated square and routes between points
    :param x: Array of X to plot
    :param y: Array of Y to plot
    :param square: Square with initial point(x0;y1) and side of square
    :param lines: List of connected cities to draw
    :return: Plot an array of points and draw square that includes as much points as possible
    """
    x1, y1, size = square
    fig = plt.figure()
    ax = fig.add_subplot(111, aspect='equal')
    ax.add_patch(Rectangle((x1, y1),
                           size, size,
                           fill=False,
                           color="r"
                           ))
    ax.scatter(x, y, marker='o', s=15)
    ax.plot(list(map(itemgetter(0), lines)), list(map(itemgetter(1), lines)), 'k', linewidth=0.5)
    plt.xlim([0, 600])
    plt.ylim([0, 400])
    plt.xticks(np.arange(0, 600 + 1, 50))
    plt.yticks(np.arange(0, 400 + 1, 50))
    plt.grid(linewidth=0.25)
    plt.title("City")
    plt.show()

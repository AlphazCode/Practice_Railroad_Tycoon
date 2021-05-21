import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from settings import width, height


def plot(x, y, square=None, lines=None):
    """
    Function to draw all points, most populated square and routes between points
    :param x: Array of X to plot
    :param y: Array of Y to plot
    :param square: Square with initial point(x0;y1) and side of square
    :param lines: List of connected cities to draw
    :return: Plot an array of points and draw square that includes as much points as possible
    """

    x_pairs = list()
    y_pairs = list()

    fig, ax = plt.subplots()
    ax.scatter(x, y, marker='o', s=15)
    if square:
        x1, y1, size = square
        ax.add_patch(Rectangle((x1, y1),
                               size, size,
                               fill=False,
                               color="r"
                               ))
    if lines is not None:
        for i in lines:
            x_pairs.append([i[0][0], i[1][0]])
            y_pairs.append([i[0][1], i[1][1]])
        for x_ends, y_ends in zip(x_pairs, y_pairs):
            ax.plot(x_ends, y_ends, 'k', linewidth=0.5)

    plt.xlim([0,width])
    plt.ylim([0, height])
    plt.ylim(max(plt.ylim()), min(plt.ylim()))
    plt.xticks(np.arange(0, width + 1, 50))
    plt.yticks(np.arange(0, height + 1, 50))
    plt.grid(linewidth=0.25)

    plt.title("City")
    plt.show()

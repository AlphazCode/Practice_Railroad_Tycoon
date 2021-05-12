from point import Point
from utils import plot
import numpy as np

def main():
    Point.create_points(10)
    x, y = Point.points_x_y()
    print(x,y)
    plot(x,y)

if __name__ == "__main__":
    main()
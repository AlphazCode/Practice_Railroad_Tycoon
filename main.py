from point import Point
from utils import plot


def main():
    Point.create_points(450)
    square = Point.most_concentration(50)
    connected_points = Point.closest_point()
    x, y = Point.points_x_y()
    plot(x, y, square, connected_points)


if __name__ == "__main__":
    main()

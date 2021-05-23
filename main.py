from script.point import Point
from script.plot import plot
from settings import square_size, point_count


def main():
    Point.create_points(point_count)
    square = Point.most_concentration(square_size)
    first = Point.first_point(Point.close_points_list)
    connected_points = Point.closest_point(first)
    print("Balance =", Point.budget * 1000)
    x, y = Point.points_x_y()
    plot(x, y, square, connected_points)


if __name__ == "__main__":
    main()

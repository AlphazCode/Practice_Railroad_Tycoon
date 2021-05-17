import numpy as np


class Point:
    points = list()
    cl_list = list()
    close_points_list = list()
    width = 600
    height = 400

    def __init__(self):
        self.x = np.random.randint(0, Point.width)
        self.y = np.random.randint(0, Point.height)

        self.coordinates = [self.x, self.y]
        Point.points.append(self)

    def __repr__(self):
        return str(self.coordinates)

    def __str__(self):
        return f"Point {self.coordinates}"

    @classmethod
    def create_points(cls, count):
        """
        :param count: How many class instances to create
        :return: Create <count> instances and stores in array
        """
        for _ in range(count):
            cls()
        cls.cl_list = cls.points[:]

    @classmethod
    def points_list(cls):
        """
        :return: List of Point instances
        """
        return np.array(cls.points)

    @staticmethod
    def points_coordinates():
        """
        :return: Combined X and Y position of Point instance
        """
        return [item.coordinates for item in Point.points]

    @classmethod
    def points_x_y(cls):
        """
        :return: Separated X and Y position of Point instance
        """
        return [item.x for item in cls.points], [item.y for item in cls.points]

    @staticmethod
    def boolean_point_list():
        """
        :return: Array with specified size <width><height> where ones represent existing of point on that co-ordinates
        """
        arr = np.zeros((Point.width, Point.height), dtype=int)
        for i in Point.points:
            arr[i.x][i.y] = 1
        return arr

    @classmethod
    def most_concentration(cls, zone_size):
        """
        Finds a square with most points groupings
        :param zone_size: Size of square to look in
        :return: Coordinates of square with the biggest concentrations of points
        """
        arr = cls.boolean_point_list()
        max_sum = int()
        row_idx, col_idx = 0, 0
        for row in range(arr.shape[0] - zone_size):
            for col in range(arr.shape[1] - zone_size):
                curr_sum = np.sum(arr[row:row + zone_size, col:col + zone_size])
                if curr_sum > max_sum:
                    row_idx, col_idx = row, col
                    max_sum = curr_sum
        print(max_sum)
        for i in cls.points:
            cls.close_points_list.append(i) if (i.x in range(row_idx, (row_idx + zone_size))) \
                                               and (i.y in range(col_idx, (col_idx + zone_size))) else None

        return row_idx, col_idx, zone_size

    @classmethod
    def min_distance(cls, point, delete_match=True):
        """
        Function to select the point closest to origin one
        :param point: Specify origin point
        :param delete_match: if True - deletes origin point from list preventing loop
        :return: min_distance, origin_point, destination_point
        """
        min_dist = 1000
        p1, p2 = None, None
        for destination_point in cls.cl_list:
            if destination_point != point:
                curr_distance = point.find_distance(destination_point)
                if curr_distance < min_dist:
                    min_dist = curr_distance
                    p1, p2 = point, destination_point

        if delete_match:
            cls.cl_list.remove(point) if point in cls.cl_list else None
        return min_dist, p1, p2

    @classmethod
    def first_point(cls):
        """
        Function to select point from most populated square
        :return: Point to start with
        """
        min_distance = 1000
        p1, p2 = None, None
        for i in cls.close_points_list:
            pnt = cls.min_distance(i, delete_match=False)
            curr_distance = pnt[0]
            if curr_distance < min_distance:
                min_distance = curr_distance
                p1, p2 = pnt[1], pnt[2]
        return p1

    @classmethod
    def closest_point(cls):
        """
        Function to find the closest point and and makes a route to this
        :return: List of connection between points
        """
        connected = list()
        price = list()
        start_point = cls.first_point()
        for i in range(len(cls.points)):
            start_point = cls.min_distance(start_point)[2]
            connected.append(start_point.coordinates) if start_point is not None else None
        print(sum(price))
        return connected

    def find_distance(self, point):
        """
        :param point: Point to find distance between
        :return: Euclidean distance between two points
        """
        # return math.sqrt(pow((point.x - self.x), 2) + pow((point.y - self.y), 2))
        return abs(self.x - point.x) + abs(self.y - point.y)

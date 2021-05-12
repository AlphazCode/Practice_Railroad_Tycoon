import math
from scipy import spatial
import numpy as np


class Point:
    points = list()
    width = 600
    height = 400

    def __init__(self):
        self.x = np.random.randint(0, Point.width + 1)
        self.y = np.random.randint(0, Point.height + 1)

        self.coords = [self.x, self.y]
        Point.points.append(self)

    def __repr__(self):
        return str(self.coords)

    def __str__(self):
        return f"Point {self.coords}"

    @classmethod
    def points_list(cls):
        return np.array(cls.points)

    @staticmethod
    def points_coordinates():
        return np.array([item.coords for item in Point.points])

    @classmethod
    def points_x_y(cls):
        return [item.x for item in cls.points], [item.y for item in cls.points]



    @classmethod
    def most_concentration(cls):
        coords = cls.points_coordinates()
        step = 50
        # for i in range(0, cls.width+1, step):
        #     for j in range(0, cls.height+1, step):
        #         for point in coords:
        #             print(coords)
        #             if (list(point) in (i, j)):
        #                 print(point)
        #                 continue
        # return cls.most_concentration(new_coords, divider * 2)

    def find_distance(self, point):
        """
        :param point: Point to find distance between
        :return: Euclidean distance between two points
        """
        return math.sqrt(pow((point.x - self.x), 2) + pow((point.y - self.y), 2))

    @classmethod
    def create_points(cls, count):
        for _ in range(count):
            cls()




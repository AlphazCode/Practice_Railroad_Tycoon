from operator import itemgetter

import numpy as np
from scipy.spatial import distance
from settings import *


class Point:
    points = np.array([])
    close_points_list = np.array([])
    points_to_be_deleted = np.array([])
    connected_points = list()
    budget = budget

    def __init__(self):
        self.x = np.random.randint(0, width)
        self.y = np.random.randint(0, height)
        self.connected = False
        self.coordinates = [self.x, self.y]
        Point.points = np.append(Point.points, [self]) if self is not None else None

    @staticmethod
    def activate_point(pnt):
        if isinstance(pnt, Point):
            pnt.connected = True
        if pnt in Point.points_to_be_deleted:
            Point.points_to_be_deleted = np.delete(Point.points_to_be_deleted,
                                                   np.where((Point.points_to_be_deleted == pnt)))

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
        cls.points_to_be_deleted = cls.points.copy()

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
        arr = np.zeros((width, height), dtype=int)
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
            if (i.x in range(row_idx, (row_idx + zone_size))) and (i.y in range(col_idx, (col_idx + zone_size))):
                cls.close_points_list = np.append(cls.close_points_list, i)
        return row_idx, col_idx, zone_size

    @classmethod
    def first_point(cls):
        """
        Function to select point from most populated square
        :return: Point to start with
        """
        diff = 30
        arr = cls.close_points_list
        p1 = None
        n = len(arr)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if arr[i].find_distance(arr[j]) < diff:
                    p1 = arr[i]
                    diff = arr[i].find_distance(arr[j])

        return p1

    @classmethod
    def closest_point(cls, point):
        """
        Function to find the closest point and and makes a route to this
        :return: List of connection between points
        """

        def point_routine(neighbour):
            cls.activate_point(neighbour)
            cls.activate_point(point)
            cls.connected_points.append([point.coordinates, neighbour.coordinates])
            cls.budget += 1
            cls.closest_point(neighbour)

        diff = 400
        closest = list()
        if cls.points_to_be_deleted.size != 0:
            for j in range(len(cls.points_to_be_deleted)):
                if (point.find_distance(cls.points_to_be_deleted[j]) < diff) \
                        and (point != cls.points_to_be_deleted[j]) \
                        and (point is not None) \
                        and (not cls.points_to_be_deleted[j].connected):
                    diff = point.find_distance(cls.points_to_be_deleted[j])
                    closest.append([point.find_distance(cls.points_to_be_deleted[j]), cls.points_to_be_deleted[j]])
                else:
                    continue
        for i in range(len(cls.points_to_be_deleted)):
            if cls.points_to_be_deleted[i].connected:
                np.delete(cls.points_to_be_deleted, i)
        if len(closest) != 0:
            closest = sorted(closest, key=lambda x: x[0])
            index = np.array(list(map(itemgetter(0), closest))).searchsorted(-1)
            if index:
                closest = closest[:index]
            else:
                closest = closest[0]

        try:
            mileage = sum(list(map(itemgetter(0), closest)))
            list_close_points = list(map(itemgetter(1), closest))
        except TypeError:
            mileage, list_close_points = closest
        cls.budget -= mileage * 5

        if isinstance(list_close_points, Point):
            point_routine(list_close_points)
        else:
            for i in list_close_points:
                point_routine(i)

        return cls.connected_points

    def find_distance(self, point):
        """
        :param point: Point to find distance between
        :return: Euclidean distance between two points
        """
        return int(distance.euclidean(self.coordinates, point.coordinates if isinstance(point, Point) else point))

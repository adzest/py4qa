__author__ = 'oleksii.isakov'

from math import sqrt


class Point:
    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance(self, int_end_point):
        dx = int_end_point.x - self.x
        dy = int_end_point.y - self.y
        return sqrt(dx * dx + dy * dy)

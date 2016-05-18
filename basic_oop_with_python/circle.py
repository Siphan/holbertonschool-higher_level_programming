import math

class Circle():
    def __init__(self, radius):
        self._radius = radius

    def get_color(self):
        return self._color

    def get_center(self):
        return self._center

    def set_color(self, color):
        self._color = color

    def set_center(self, center):
        self._color = center

    def area(self):
        return self._radius ** 2 * math.pi

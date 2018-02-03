import os


class Circle(object):
    def __init__(self):
        self.__radius = 1.1

    def get_radius(self):
        return self.__radius


class Rect(Circle):
    def get_radius(self):
        return super(Rect, self).get_radius()



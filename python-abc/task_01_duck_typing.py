#!/usr/bin/python3
"""Define 3 classes (Shape, Circle, Rectangle)"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class

    Args:
        ABC (class): used to create abstract methods.
    """

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle class.

    Args:
        Shape (class): To inherit from.
    """

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return (math.pi * self.radius ** 2)

    def perimeter(self):
        return (2 * math.pi * self.radius)


class Rectangle(Shape):
    """Rectangle class

    Args:
        Shape (class): to inherit from.
    """

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        return (2 * (self.height + self.width))


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

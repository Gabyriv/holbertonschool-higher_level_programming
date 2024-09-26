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
        self.__radius = radius

    def area(self):
        return (math.pi * self.__radius ** 2)

    def perimeter(self):
        return (2 * math.pi * abs(self.__radius))


class Rectangle(Shape):
    """Rectangle class

    Args:
        Shape (class): to inherit from.
    """

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__height + self.__width))


def shape_info(shape):
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")

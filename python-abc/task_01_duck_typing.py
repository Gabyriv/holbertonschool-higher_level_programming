#!/usr/bin/python3
"""Module defining abstract Shape class and
    concrete Circle and Rectangle classes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.

    Defines the interface that all shape subclasses must implement.
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.

        This method must be implemented by subclasses.

        :return: The area of the shape.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.

        This method must be implemented by subclasses.

        :return: The perimeter of the shape.
        """
        pass


class Circle(Shape):
    """
    Class representing a circle.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initialize the Circle with a specific radius.

        :param radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        Formula: π * radius²

        :return: The area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the circumference of the circle.

        Formula: 2 * π * radius

        :return: The circumference of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Class representing a rectangle.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize the Rectangle with a specific width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        Formula: width * height

        :return: The area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        Formula: 2 * (width + height)

        :return: The perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of a shape.

    This function uses duck typing and assumes that the passed object has
    both `area` and `perimeter` methods implemented.

    :param shape: A shape object with area and perimeter methods.
    """
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


if __name__ == "__main__":
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)

    shape_info(circle)
    shape_info(rectangle)

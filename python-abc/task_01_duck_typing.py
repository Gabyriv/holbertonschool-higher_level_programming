#!/usr/bin/python3

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class that defines the interface for all shape objects.

    This class mandates that any subclass must implement the `area` and `perimeter` methods.
    """

    @abstractmethod
    def area(self):
        """
        Compute the area of the shape.

        This method must be implemented by any subclass of Shape.

        :return: The area of the shape as a float.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Compute the perimeter of the shape.

        This method must be implemented by any subclass of Shape.

        :return: The perimeter of the shape as a float.
        """
        pass


class Circle(Shape):
    """
    A class representing a circle, inheriting from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius: float):
        """
        Initialize a Circle with the given radius.

        :param radius: The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculate the area of the circle.

        The formula used is: π * radius^2

        :return: The area of the circle as a float.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        The formula used is: 2 * π * radius

        :return: The perimeter of the circle as a float.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A class representing a rectangle, inheriting from Shape.

    Attributes:
        width (float): The width of the rectangle.
        height (float): The height of the rectangle.
    """

    def __init__(self, width: float, height: float):
        """
        Initialize a Rectangle with the given width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Calculate the area of the rectangle.

        The formula used is: width * height

        :return: The area of the rectangle as a float.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.

        The formula used is: 2 * (width + height)

        :return: The perimeter of the rectangle as a float.
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Display the area and perimeter of a given shape.

    This function relies on duck typing, assuming that the passed object
    implements both the `area()` and `perimeter()` methods.

    :param shape: An object representing a shape. It is assumed that this object has
                  `area()` and `perimeter()` methods.
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")


# Create instances of Circle and Rectangle
circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=7)

# Test the shape_info function
shape_info(circle)
shape_info(rectangle)

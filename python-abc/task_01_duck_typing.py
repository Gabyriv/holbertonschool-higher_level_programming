#!/usr/bin/python3
"""Define an abstract class."""


from abc import ABC, abstractmethod


class Shape():
    """Shape class."""
    @abstractmethod
    def area(self):
        """Area method"""
        pass

    @abstractmethod
    def perimeter(self):
        """Perimeter method"""
        pass


class Circle(Shape):
    """Circle class.

    Args:
        Shape (class): An abstract class.
    """

    def __init__(self, radius):
        """Constructor

        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius

    def area(self):
        """Calculates the area of a circle.

        Returns:
            float: The area of a circle.
        """
        return (3.14 * self.radius ** 2)

    def perimeter(self):
        """Calculates the circumference of a circle.

        Returns:
            float: The circumference of a circle.
        """
        return (2 * 3.14 * self.radius)


class Rectangle(Shape):
    """Rectangle class.

    Args:
        Shape (class): An abstract class.
    """

    def __init__(self, width, height):
        """Constructor.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.width = width
        self.height = height

    def area(self):
        """Calculates the area of a rectangle.

        Returns:
            int: the area of the rectangle.
        """
        return (self.width * self.height)

    def perimeter(self):
        """Calculates the perimeter of a rectangle

        Returns:
            int: the perimeter of the rectangle
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")


circle = Circle(5)
rectangle = Rectangle(4, 7)

shape_info(circle)
shape_info(rectangle)

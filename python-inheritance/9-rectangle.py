#!/usr/bin/python3
"""Define a class that inherits from BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class that inherits from BaseGeometry.

    Args:
        BaseGeometry (class): class defined in 5-base_geometry.py.
    """

    def __init__(self, width, height):
        """Instantiation with width and height

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)

    def area(self):
        """Function that calculates the area of a rectangle.

        Returns:
            int: the area of the rectangle.
        """
        return (self.__width * self.__height)

    def __str__(self):
        """Returns the following description: [Rectangle] <width>/<height>
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")

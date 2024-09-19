#!/usr/bin/python3
"""Define a class named Rectangle."""


class Rectangle:
    """This class represents a rectangle."""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instantiation with optionals.

        Args:
            width (int, optional): The width of the rectangle. Defaults to 0.
            height (int, optional): The height of the rectangle. Defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Function to retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Function to set the width of the rectangle.

        Args:
            value (int): must be an int.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Function to retrieve the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Function to set the height of the rectangle.

        Args:
            value (int): must be an int.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """This function returns the area of a rectangle."""
        return (self.__height * self.__width)

    def perimeter(self):
        """This function returns the perimeter of a rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__height + self.__height + self.__width + self.__width)

    def __str__(self):
        """Function that prints the rectangle with the # characters.

        Returns:
            str: # character * height * width.
        """
        if self.__height == 0 or self.__width == 0:
            return ("")
        else:
            symbol = str(self.print_symbol)
            return "\n".join([symbol * self.__width
                              for i in range(self.__height)])

    def __repr__(self):
        """
        This function should return a string representation
            of the rectangle to be able to recreate a new instance.

        Returns:
            str: a string representation of the rectangle.
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle based on the area

        Args:
            rect_1: must be an instance of rectangle
            rect_2: must be an instance of rectangle

        Raises:
            TypeError: if rect_1 or rect_2 is not an instance of Rectangle.

        Returns:
            rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")

        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)

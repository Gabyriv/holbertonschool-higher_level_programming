#!/usr/bin/python3

"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Initialize a square.

        Args:
            size (int, optional): Private instance attribute. Defaults to 0.

        Raises:
            TypeError: if size isn't an integer.
            ValueError: if size < 0
        """
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """function to get the area of a square

        Returns:
            int: the size of the square
        """
        return (self.__size ** 2)

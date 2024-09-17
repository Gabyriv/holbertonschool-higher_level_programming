#!/usr/bin/python3

"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0):
        """Instantiation with optional

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.size = size

    @property
    def size(self):
        """Function to retrieve the size of a square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        """This function is to set the size of the square.

        Args:
            value (int): must be an integer.

        Raises:
            TypeError: if value is not an int.
            ValueError: if value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be an integer")
        self.__size = value

    def area(self):
        """Function that gets the area of a square.

        Returns:
            int: the area of the square.
        """
        return (self.__size ** 2)

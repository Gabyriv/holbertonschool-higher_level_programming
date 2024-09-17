#!/usr/bin/python3

"""Define a class named Square."""


class Square:
    """This class represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Instantiation with optionals.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
            position (tuple, optional): Position . Defaults to (0, 0).
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Function to retrieve the position"""
        return (self._position)

    @position.setter
    def position(self, value):
        """function to set the position.

        Args:
            value (tuple): must be a tuple of 2 positive integers.

        Raises:
            TypeError: if value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Function that gets the area of a square.

        Returns:
            int: the area of the square.
        """
        return (self.__size ** 2)

    def my_print(self):
        """Function that prints a # for the size of the square."""
        if self.size == 0:
            print()
            return
        for j in range(self.__position[1]):
            print()
        for i in range(self.size):
            print(" " * self.__position[0] + "#" * self.__size)

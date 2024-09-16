#!/usr/bin/python3

"""Creating a Class named Square"""


class Square:
    def __init__(self, size=0):
        """defining the square by size.

        Args:
            size (int, optional): private instance attribute. Defaults to 0.
        """
        self.__size = size

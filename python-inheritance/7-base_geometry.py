#!/usr/bin/python3
"""Define an geometry class"""


class BaseGeometry:
    """Geometry class"""

    def area(self):
        """
        A public instance method.

        Raises:
            Exception: with the message area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value.

        Args:
            name (str): You can assume is always a string.
            value (int): value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value <= 0.
        """
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

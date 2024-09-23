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

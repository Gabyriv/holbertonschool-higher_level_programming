#!/usr/bin/python3
"""Define a function to check if an obj is an instance of a specified class"""


def is_same_class(obj, a_class):
    """Checks if an obj is exactly an instance of the specified class.

    Args:
        obj: an object
        a_class: a class

    Returns:
        True: if the object is exactly an instance of the specified class.
        False: otherwise.
    """
    return type(obj) is a_class

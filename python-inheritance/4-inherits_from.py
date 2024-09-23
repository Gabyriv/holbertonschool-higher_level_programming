#!/usr/bin/python3
"""Define a function"""


def inherits_from(obj, a_class):
    """Checks if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class.

    Args:
        obj: an object
        a_class: a class

    Returns:
        True: if obj is an instance of a class that inherited from a_class.
        False: Otherwise.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class

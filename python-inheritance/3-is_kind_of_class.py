#!/usr/bin/python3
"""Define a function"""


def is_kind_of_class(obj, a_class):
    """Checks if the object is an instance of, or
        if the object is an instance of a
        class that inherited from, the specified class.

    Args:
        obj: an object
        a_class: a class
    """
    return isinstance(obj, a_class)

#!/usr/bin/python3
"""Define a function that returns the dictionary description with
simple data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object"""


import json


def class_to_json(obj):
    """Return the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON serialization
    of an object.

    Args:
        obj (object): The object to serialize.

    Returns:
        dict: The dictionary description of the object.
    """
    return obj.__dict__

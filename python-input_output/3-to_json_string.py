#!/usr/bin/python3
"""Define a function that returns the JSON representation of an obj"""


import json


def to_json_string(my_obj):
    """Returns a JSON string representation of a given object.

    Args:
        my_obj (object): The object to convert to a JSON string.

    Returns:
        str: A JSON string representation of my_obj.
    """
    return json.dumps(my_obj)

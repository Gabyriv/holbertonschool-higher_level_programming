#!/usr/bin/python3
"""Define a function that returns an obj(Python data structure) represented by a JSON string"""

import json


def from_json_string(my_str):
    """Return an object(Python data structure) represented by a JSON string

    Args:
        my_str (str): a JSON string representation of an object
    Returns:
        object: a Python object
    """
    return json.loads(my_str)

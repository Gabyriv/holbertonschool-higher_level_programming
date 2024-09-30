#!/usr/bin/python3
"""Define a function that creates an Obj from a JSON file"""


import json


def load_from_json_file(filename):
    """Create an object from a JSON file.

    Args:
        filename (str): The JSON file to read from.

    Returns:
        object: The object represented by the JSON file.
    """
    with open(filename) as f:
        return json.load(f)

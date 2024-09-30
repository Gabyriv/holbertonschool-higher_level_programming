#!/usr/bin/python3
"""Define a function that writes an Object to a text file,
using a JSON representation."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation.

    Args:
        my_obj (object): Object to be written to the text file.
        filename (str): Name of the file to write to.
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)

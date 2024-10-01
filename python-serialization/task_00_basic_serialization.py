#!/usr/bin/python3
"""Basic Serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Save a serialized data to a file

    Args:
        data (object): A Python dictionary with data
        filename (str): The file name of the output JSON file,
                        if the output file exists, it should be replaced
    """
    with open(filename, 'w') as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    Load a serialized data from a file

    Args:
        filename (str): The filename of the input JSON file

    Returns:
        dict: A Python dictionary with the deserialized JSON data
                from the file
    """
    with open(filename, 'r') as file:
        return json.load(file)

#!/usr/bin/python3
"""Append a string to the end of a text file"""


def append_write(filename="", text=""):
    """Append a string to the end of a text file

    Args:
        filename (str): file to write to (default is empty string)
        text (str): string to write to file (default is empty string)

    Returns:
        int: the number of characters written
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)

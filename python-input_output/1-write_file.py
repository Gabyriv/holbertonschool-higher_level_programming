#!/usr/bin/python3
"""Defines a function that writes a string to a text file."""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Args:
        filename (str): The file to write. Defaults to "".
        text (str): The text to write to the file. Defaults to "".
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        w_content = f.write(text)
    return w_content

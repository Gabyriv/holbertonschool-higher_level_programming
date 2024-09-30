#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename (str): name of file to read. Defaults to "".
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")

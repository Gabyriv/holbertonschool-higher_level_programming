#!/usr/bin/python3
"""Read a file"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
        filename (str): name of file to read. Defaults to "".
    """
    with open('my_file_0.txt', encoding="utf-8") as file:
        file_read = file.read()
        print(file_read, end="")

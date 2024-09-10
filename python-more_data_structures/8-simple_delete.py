#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """
    Function that deletes a key in a dictionary

    Args:
        a_dictionary (dictionary): Is the dictionary containing the data
        key (str, argument): Will always be a string. Defaults to "".
    """

    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary

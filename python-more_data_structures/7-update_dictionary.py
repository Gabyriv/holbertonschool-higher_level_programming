#!/usr/bin/python3

def update_dictionary(a_dictionary, key, value):
    """
    Function that replace or adds key/value in a dictionary

    Args:
        a_dictionary: a dictionary
        key (argument): will always be a string
        value (argument): will be any type
    """

    a_dictionary[key] = value
    return a_dictionary

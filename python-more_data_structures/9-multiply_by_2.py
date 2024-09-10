#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dictionary = {}

    for i in a_dictionary:
        original = a_dictionary[i]
        multiplied = original * 2
        new_dictionary[i] = multiplied
    return new_dictionary

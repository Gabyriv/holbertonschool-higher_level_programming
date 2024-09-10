#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or not a_dictionary:
        return None

    # Initialize variables to keep track of the best score and corresponding key
    best_key = None
    best_value = -float('inf')  # this is to start with the smallest possible value

    for key, value in a_dictionary.items():
        if value > best_value:
            best_value = value
            best_key = key

    return best_key

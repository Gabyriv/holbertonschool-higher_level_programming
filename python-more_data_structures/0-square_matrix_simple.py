#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_element = []
    for row in matrix:
        new_row = []
        for x in row:
            new_row.append(x ** 2)
        new_element.append(new_row)
    return new_element

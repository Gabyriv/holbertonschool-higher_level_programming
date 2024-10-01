#!/usr/bin/python3
"""Create a function that returns a list of lists of integers
representing the Pascal's triangle of n."""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    the Pascal's triangle of n.

    Args:
        n (int): The size of the triangle

    Returns:
        list: A list of lists of integers representing
              the Pascal's triangle of n
    """
    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j] + triangle[i - 1][j - 1])
        row.append(1)
        triangle.append(row)
    return triangle

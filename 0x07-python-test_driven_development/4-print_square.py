#!/usr/bin/python3
"""
print_square - function that prints a square with the character #.
"""

def print_square(size):
    """
    args:
        square (int): the size of the square.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for row in range(size):
        for column in range(size):
            print("#", end="")
        print()

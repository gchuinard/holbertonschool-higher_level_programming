#!/usr/bin/python3
"""
add_integer - function that adds 2 integers.
"""


def add_integer(a, b=98):
    """
    args:
        a (int, float): the first integer.
        b (int, float): the second integer.
    return: the sun of a + b in integer or raise error if fail.
    """

    if a == float("inf") or a == float("-inf"):
        raise TypeError("a must be an integer")
    if b == float("inf") or b == float("-inf"):
        raise TypeError("b must be an integer")
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return int(a) + int(b)

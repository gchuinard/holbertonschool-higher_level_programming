#!/usr/bin/python3
"""
This is class module: Square
"""


class Square:
    """
    Define a square
    """

    def __init__(self, size=0):
        """
        The constructor
        args:
            size (int): square size
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

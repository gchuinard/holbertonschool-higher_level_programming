#!/usr/bin/python3
"""
class Square
"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """
    inherits from Rectangle
    """

    def __init__(self, size):
        """
        constructor of Square
        """
        super().__init__(size, size)
        self.__size = size


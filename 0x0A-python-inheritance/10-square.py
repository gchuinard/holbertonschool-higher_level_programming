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
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        """
        return the description of the square
        """

        return "[Rectangle] {:d}/{:d}".format(self.__size, self.__size)

    def area(self):
        """
        return the area of the square
        """

        return self.__size ** 2

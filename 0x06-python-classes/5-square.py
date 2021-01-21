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
        self.size = size

    def area(self):
        return self.__size**2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        size_p = self.__size
        if size_p == 0:
            print()
        else:
            for row in range(size_p):
                for column in range(size_p):
                    print('#', end="")
                print()

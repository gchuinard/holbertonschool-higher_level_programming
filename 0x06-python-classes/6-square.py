#!/usr/bin/python3
"""
This is class module: Square
"""


class Square:
    """
    Define a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        The constructor
        args:
            size (int): square size
        """
        self.size = size
        self.position = position

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
        pos = self.__position
        if size_p == 0:
            print()
        else:
            for ret in range(pos[1]):
                print()
            for row in range(size_p):
                for sps in range(pos[0]):
                    print(" ", end="")
                for column in range(size_p):
                    print('#', end="")
                print()

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

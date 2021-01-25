#!/usr/bin/python3
"""
This is the rectangle module.
"""


class Rectangle:
    """
    Create the class Rectangle.
    """

    def __init__(self, width=0, height=0):
        """
        args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height

    def __str__(self):
        """
        the representation of the object in string
        """
        string = ""
        if self.__height > 0 and self.__width > 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += "#"
                if h < self.__height - 1:
                    string += "\n"
        return string

    @property
    def width(self):
        """
        getter of width
        """
        return self.__width

    @property
    def height(self):
        """
        getter of height
        """
        return self.__height

    @width.setter
    def width(self, value):
        """
        setter of width
        args:
            value (int): new width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter of height
        args:
            value (int): new height value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        calcul the area of the rectangle.
        return: the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        calcul the perimeter of the rectangle.
        return: the perimeter of the rectangle.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

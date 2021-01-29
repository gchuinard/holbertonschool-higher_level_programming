#!/usr/bin/python3
"""
class Rectangle
"""

from models.base import Base

class Rectangle(Base):
    """
    The class Rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor of Rectangle
        """

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

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

    @property
    def x(self):
        """
        getter of x
        """

        return self.__x

    @property
    def y(self):
        """
        getter of y
        """

        return self.__y

    @width.setter
    def width(self, value):
        """
        setter of width
        """

        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter of height
        """

        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter of x
        """

        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter of y
        """

        self.__y = value

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

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """
        return the description of rectangle in string
        """

        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id,
                                                                 self.x,
                                                                 self.y,
                                                                 self.width,
                                                                 self.height)

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

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """
        setter of height
        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """
        setter of x
        """

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """
        setter of y
        """

        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area of the rectangle
        """

        return self.__width * self.__height

    def display(self):
        """
        prints in stdout the Rectangle instance with the character #
        """
        for a in range(self.__y):
            print()
        for h in range(self.__height):
            for o in range(self.__x):
                print(" ", end="")
            for w in range(self.__width):
                print("#", end="")
            print()

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """

        attributes = ["id", "width", "height", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for i, arg in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, arg)

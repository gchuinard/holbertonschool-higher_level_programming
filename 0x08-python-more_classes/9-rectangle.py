#!/usr/bin/python3
"""
This is the rectangle module.
"""


class Rectangle:
    """
    Create the class Rectangle.
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        args:
            width (int): the width of the rectangle.
            height (int): the height of the rectangle.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1
        self.print_symbol = Rectangle.print_symbol

    def __str__(self):
        """
        the representation of the object in string
        return: the string
        """
        string = ""
        if self.__height > 0 and self.__width > 0:
            for h in range(self.__height):
                for w in range(self.__width):
                    string += str(self.print_symbol)
                if h < self.__height - 1:
                    string += "\n"
        return string

    def __repr__(self):
        """
        method returns a string containing a printable representation
        of an object.
        return: the string
        """
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)

    def __del__(self):
        """
        delete an instance of the object
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def bigger_or_equal(rect_1, rect_2):
        """
        args:
            rect_1: instance of Rectangle.
            rect_2: instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        return rect_2 if rect_1.area() < rect_2.area() else rect_1

    @classmethod
    def square(cls, size=0):
        """
        that returns a new Rectangle instance.
        return: a new instance of Rectangle.
        """
        return cls(size, size)

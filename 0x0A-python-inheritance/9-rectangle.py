#!/usr/bin/python3
"""
class Rectangle
"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    inherits from BaseGeometry
    """

    def __init__(self, width, height):
        """
        constructor of Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """
        return the description of the rectangle
        """

        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

    def area(self):
        """
        return the area of the rectangle
        """

        return self.__width * self.__height

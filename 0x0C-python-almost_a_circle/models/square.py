#!/usr/bin/python3
"""
class Square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The class Square
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        constructor of Rectangle
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        return the description of square in string
        """

        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id,
                                                         self.x,
                                                         self.y,
                                                         self.width)

    @property
    def size(self):
        """
        getter of size
        """

        return self.width

    @size.setter
    def size(self, value):
        """
        setter of size
        """

        self.width = value
        self.height = value

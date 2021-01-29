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

    def update(self, *args, **kwargs):
        """
        assigns an argument to each attribute
        """

        attributes = ["id", "size", "x", "y"]

        if args:
            for i, arg in enumerate(args):
                setattr(self, attributes[i], arg)
        else:
            for i, arg in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, arg)

        def to_dictionary(self):
            """
            returns the dictionary representation of a Rectangle
            """
 
            return {
                    "id": self.id,
                    "size": self.size,
                    "x": self.x,
                    "y": self.y
                    }

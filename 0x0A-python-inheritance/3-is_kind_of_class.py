#!/usr/bin/python3
"""
class MyList
"""


def is_same_class(obj, a_class):
    """
    returns True if the object is an instance of, or if the object
    is an instance of a class that inherited from, the specified class;
    otherwise False.
    """

    return isinstance(obj) is a_class

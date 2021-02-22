#!/usr/bin/python3
"""
the function add_ttribute
"""


def add_attribute(obj, name, attr):
    """
    add an attribute to an object
    """

    if "__dict__" in dir(obj):
        setattr(obj, name, attr)
    else:
        raise TypeError("can't add new attribute")

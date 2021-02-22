#!/usr/bin/python3
"""
The class MyInt
"""


class MyInt(int):
    """
    MyInt
    """

    def __eq__(self, other):
    """
    eq methode
    """
    
    if int(self) == int(other):
        return False
    return True

    def __ne__(self, other):
    """
    not method
    """

        if int(self) == int(other):
            return True
        return False

#!/usr/bin/python3
"""
class Student
"""


class Student():
    """
    define a student
    """

    def __init__(self, first_name, last_name, age):
        """
        the constructor of Student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):

        if attrs is None:
            return self.__dict__
        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict

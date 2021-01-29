#!/usr/bin/python3
"""
class Base
"""

import json


class Base():
    """
    class Base
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor of Base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns the JSON string representation of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == "":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation of list_objs to a file
        """
        
        new_list = []
        if list_objs is not None:
            for i in list_objs:
                new_list.append(i.to_dictionary())

        with open(cls.__name__ + ".json", 'w+', encoding="utf-8") as f:
            f.write(cls.to_json_string(new_list))

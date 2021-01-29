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

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attributes already set
        """
        if cls.__name__ is "Rectangle":
            dum = cls(1, 1)
        elif cls.__name__ is "Square":
            dum = cls(1)
        dum.update(**dictionary)
        return dum

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

    @classmethod
    def load_from_file(cls):
        """
        returns a list of instances from a file
        """

        new_list = []
        try:
            with open(cls.__name + ".json", mode="r", encoding="utf-8") as f:
                for d in cls.from_json_string(f.read()):
                    inst_list.append(cls.create(**d))
        except:
            pass
        return new_list

    def from_json_string(json_string):
        """
        returns the list of the JSON string representation json_string
        """

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

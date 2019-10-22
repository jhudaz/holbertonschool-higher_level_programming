#!/usr/bin/python3
import json
""" model `Base`"""


class Base:
    """class `Base`"""
    __nb_objects = 0

    def __init__(self, id=None):
        """constructor

        Keyword Arguments:
            id {int} -- (default: {None})
        """
        self.id = id

    @property
    def id(self):
        """id getter"""
        return self.__id

    @id.setter
    def id(self, value):
        """id setter"""
        if value is not None:
            self.__id = value
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

    """methods"""

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        content = ""
        lst = []
        for obj in list_objs:
            lst.append(obj.to_dictionary())

        content = cls.to_json_string(lst)

        with open(file, "w", encoding="utf-8") as fle:
            fle.write(content)

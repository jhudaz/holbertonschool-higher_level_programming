#!/usr/bin/python3
import json
""" model `Base`
"""


class Base:
    """class `Base`
    """
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

    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

#!/usr/bin/bash
""" model Base
"""


class Base:
    """Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init

        Keyword Arguments:
            id {int} -- id of every object (default: {None})
        """
        self.id = id

    @property
    def id(self):
        """id getter
        """
        return self.__id

    @id.setter
    def id(self, value):
        """id setter

        Arguments:
            value {int} -- new value
        """
        if value is not None:
            self.__id = value
        else:
            Base.__nb_objects += 1
            self.__id = Base.__nb_objects

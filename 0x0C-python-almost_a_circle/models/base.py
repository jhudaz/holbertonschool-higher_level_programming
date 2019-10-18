#!/usr/bin/python3
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

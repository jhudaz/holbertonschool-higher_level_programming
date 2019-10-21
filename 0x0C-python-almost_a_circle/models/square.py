#!/usr/bin/python3
"""model `Rectangle`"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """return a string with the data passed"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

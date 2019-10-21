#!/usr/bin/python3
"""model `Rectangle`"""
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        """constructor"""
        super().__init__(size, size, x, y, id)

    """getters"""

    @property
    def size(self):
        """size getter"""
        return self.width

    """setters"""

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.width = value
        self.height = value

    """methods"""

    def __str__(self):
        """return a string with the data passed"""
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

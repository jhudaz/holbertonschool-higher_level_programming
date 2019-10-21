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
        return super().width

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

    def update(self, *args, **kwargs):
        """update the attributes"""
        if len(args) > 0:
            if args[0] is not None:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                self.height = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        elif len(kwargs) > 0:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.height = kwargs['size']
                self.width = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

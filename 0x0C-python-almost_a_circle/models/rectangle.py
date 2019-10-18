#!/usr/bin/python3
"""model `Rectangle`"""
from models.base import Base


class Rectangle(Base):
    """class `Rectangle`"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor

        Arguments:
            width {int}
            height {int}

        Keyword Arguments:
            x {int} -- (default: {0})
            y {int} -- (default: {0})
            id {[type]} -- super attribute (default: {None})
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    """getters"""
    @property
    def width(self):
        """width getter"""
        return self.__width

    @property
    def height(self):
        """height getter"""
        return self.__height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @property
    def y(self):
        """y getter"""
        return self.__y

    """setters"""

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) != int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) != int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')
        self.__height = value

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) != int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) != int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    """methods"""

    def area(self):
        """return the area using the width and height"""
        return self.__height * self.__width

    def display(self):
        """display a rectangle"""
        for i in range(self.__height):
            print(self.__width * "#")

    def __str__(self):
        """"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

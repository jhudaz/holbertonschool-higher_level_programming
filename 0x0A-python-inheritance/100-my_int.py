#!/usr/bin/python3
"""
module `Int` - that modify two magic methods from int class
"""


class MyInt(int):
    """
    class MyInt - with two methods
    """

    def __eq__(self, value):
        """
        return true is two integeres are diferent
        """
        return int(self) != int(value)

    def __ne__(self, value):
        """
        return false is two integeres are equal
        """
        return int(self) == int(value)

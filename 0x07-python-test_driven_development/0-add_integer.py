#!/usr/bin/python3

""" module "adds"
add module supplies one function, add_integer().  For example,
>>> add_integer(2, 98)
100
"""


def add_integer(a, b=98):
    """
    Return the add from two numbers
    """
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    if a > 1e100:
        raise OverflowError
    if b > 1e100:
        raise OverflowError
    return int(a) + int(b)

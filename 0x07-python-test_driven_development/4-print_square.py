#!/usr/bin/python3

""" module "square"
square module supplies one function, print_square().  For example,
>>> print_square
#
"""


def print_square(size):
    """
    Return  a square of '#'
    """
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

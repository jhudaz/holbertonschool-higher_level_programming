#!/usr/bin/python3

""" module "name"
name module supplies one function, say_my_name().  For example,
>>> say_my_name("Walter", "White")
My name is Walter White
"""


def say_my_name(first_name, last_name=""):
    """
    return a string of a full name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))

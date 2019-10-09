#!/usr/bin/python3

"""
module "text"
text module supplies one function:
text_indentation()
"""


def text_indentation(text):
    """
    Return a string with indentation
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    t = text.replace('.', '.\n\n')
    t = t.replace(':', ':\n\n')
    t = t.replace('?', '?\n\n')
    t = t.replace('\n ', '\n')
    print(t)

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
    newStr1 = text.replace('.', '.\n\n')
    newStr2 = newStr1.replace(':', ':\n\n')
    newStr3 = newStr2.replace('?', '?\n\n')
    lst = newStr3.split('\n\n')
    if len(lst[-1]) == 0:
        del(lst[-1])
    for i in lst:
        print(i.lstrip(), end="")
        if i == lst[-1] and i != ':' and i != '.' and i != '?':
            break
        print('\n')

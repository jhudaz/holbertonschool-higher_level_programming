#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    k = ""
    for key in a_dictionary:
        if value == a_dictionary[key]:
            k = key
    if len(k) > 0:
        a_dictionary.pop(k)
    return a_dictionary

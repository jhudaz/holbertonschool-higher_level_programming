#!/usr/bin/python3
def uniq_add(my_list=[]):
    uniq = set(my_list)
    add = 0
    for value in uniq:
        add += value
    return add

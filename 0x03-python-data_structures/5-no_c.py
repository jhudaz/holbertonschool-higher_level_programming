#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for i in range(len(my_string)):
        if my_string[i] != 'C' or my_string[i] != 'c':
            new_str = my_string[i]
        else:
            pass

    return new_str

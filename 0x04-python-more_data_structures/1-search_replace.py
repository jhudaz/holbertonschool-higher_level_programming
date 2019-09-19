#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return [replace if search is value else value for value in my_list]

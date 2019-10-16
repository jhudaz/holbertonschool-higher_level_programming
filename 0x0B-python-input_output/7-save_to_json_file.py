#!/usr/bin/python3
import json


def save_to_json_file(my_obj, filename):
    """ save_to_json_file
    Args:
        my_obj (any): data
        filename (any): file name

    Returns:
        create a new file
    """
    with open(filename, 'w+', encoding='utf-8') as file:
        json.dump(my_obj, file)

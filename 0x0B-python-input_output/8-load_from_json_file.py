#!/usr/bin/python3
import json


def load_from_json_file(filename):
    """ load_from_json_file
    Args:
        filename (any): file name

    Returns:
        create a file from a JSON
    """
    with open(filename, 'r')as file:
        return json.load(file)

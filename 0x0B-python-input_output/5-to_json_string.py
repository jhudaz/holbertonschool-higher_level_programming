#!/usr/bin/python3
import json


def to_json_string(my_obj):
    """ to_json_string
    Args:
        my_obj (dict): dictionary

    Returns:
        a JSON
    """
    return json.dumps(my_obj)

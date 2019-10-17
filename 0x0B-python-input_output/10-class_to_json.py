#!/usr/bin/python3
def class_to_json(obj):
    """ class_to_json
    Args:
        obj (any): data

    Returns:
        dictionary
    """
    return obj.__dict__

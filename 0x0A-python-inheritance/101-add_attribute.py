#!/usr/bin/python3
def add_attribute(cls, attribute, value):
    """function that handle if we can't set an attribute
    Args:
        attribute (any): attribute name
        value (any): value for the attribute

    Returns:
        Nothing
    """
    if hasattr(cls, attribute):
        raise TypeError("can't add new attribute")
    else:
        setattr(cls, attribute, value)

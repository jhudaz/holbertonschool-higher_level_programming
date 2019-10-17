#!/usr/bin/python3
def read_file(filename=""):
    """ read-file print the file content
    Args:
        filename (path): file path

    Returns:
        Nothing
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")

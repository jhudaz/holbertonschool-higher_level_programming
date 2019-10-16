#!/usr/bin/python3
def write_file(filename="", text=""):
    """ write_file
    Args:
        filename (path): file path
        text (str): string

    Returns:
        write a string in a new file
    """
    with open(filename, mode='w', encoding='utf-8') as file:
        return file.write(text)

#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """ read_lines
    Args:
        filename (path): file path
        nb_lines (int): number of lines

    Returns:
        read the lines a print to stdout
    """
    with open(filename, encoding='utf-8') as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for i in range(nb_lines):
                print(file.readline(), end="")

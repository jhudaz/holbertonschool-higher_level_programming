#!/usr/bin/python3
def number_of_lines(filename=""):
    """ number_of_lines
    Args:
        filename (path): file path

    Returns:
        Number of lines
    """
    with open(filename, encoding='utf-8') as file:
        data = file.read()
        count = 0
        for i in range(len(data)):
            if data[i] == "\n":
                count += 1
        return count
    file.close()

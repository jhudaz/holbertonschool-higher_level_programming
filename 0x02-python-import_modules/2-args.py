#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(1, argv.__getitem__(1)))
    elif len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv.__getitem__(i)))
    else:
        print("{} arguments.".format(len(argv) - 1))

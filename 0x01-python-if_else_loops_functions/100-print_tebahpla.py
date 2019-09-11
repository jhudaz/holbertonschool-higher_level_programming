#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        n = chr(i)
    else:
        n = chr(i-32)
    print("{}".format(n), end="")

#!/usr/bin/python3
def remove_char_at(str, n):
    newStr = ""
    for i in range(len(str)):
        if i == n:
            continue
        else:
            newStr += str[i]
    return newStr

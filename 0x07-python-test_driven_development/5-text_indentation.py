#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in range(len(text)):

        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            print('\n')
        else:
            print(text[i], end="")

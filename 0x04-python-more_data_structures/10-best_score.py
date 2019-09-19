#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    else:
        name = ''
        score = 0
        for key in a_dictionary:
            if a_dictionary[key] > score:
                name = key
                score = a_dictionary[key]
    return name

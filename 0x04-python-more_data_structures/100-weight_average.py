#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    else:
        average = 0
        values = 0
        for i in my_list:
            values += (i[0] * i[1])
            average += (i[1])
    return values / average

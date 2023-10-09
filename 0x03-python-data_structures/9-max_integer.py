#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    else:
        Max = 1
        for y in my_list:
            if y > Max:
                Max = y
        return Max

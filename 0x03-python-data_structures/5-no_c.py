#!/usr/bin/env python3
def no_c(my_string):
    my_str = ""
    for i in my_string:
        if i == 'c' or i == 'C':
            continue
        else:
            my_str = my_str + i
    return my_str

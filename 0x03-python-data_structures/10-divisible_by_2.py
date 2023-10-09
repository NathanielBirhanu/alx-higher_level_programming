#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    arr = []
    for x in my_list:
        if x % 2 == 0:
            arr.append(True)
        else:
            arr.append(False)
    return (arr)

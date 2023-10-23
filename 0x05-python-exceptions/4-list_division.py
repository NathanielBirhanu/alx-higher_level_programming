#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for i in range(list_length):
        try:
            dividend = my_list_1[i]
        except IndexError:
            print("out of range")
            result.append(0)
            continue

        try:
            divisor = my_list_2[i]
        except IndexError:
            print("out of range")
            result.append(0)
            continue

        try:
            division_result = dividend / divisor
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
            continue
        except (TypeError, ValueError):
            print("wrong type")
            result.append(0)
            continue

        result.append(division_result)

    return result

#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    result = 0
    n = len(roman_string)

    for i in range(n - 1, -1, -1):
        if i < n - 1 and roman_values[roman_string[i]] < roman_values[roman_string[i + 1]]:
            result -= roman_values[roman_string[i]]
        else:
            result += roman_values[roman_string[i]]

    return result

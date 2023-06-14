#!/usr/bin/python3
def roman_to_int(roman_string):
    a = roman_string[:]
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    number = 0
    for i in range(len(a)):
        if i + 1 < len(a) and roman_numbers[a[i]] < roman_numbers[a[i + 1]]:
            number -= roman_numbers[a[i]]
        else:
            number += roman_numbers[a[i]]
    return number

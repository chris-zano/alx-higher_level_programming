#!/usr/bin/python3
def roman_to_int(roman_string):
    a = roman_string[:]
    roman_numbers = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                     'C': 100, 'D': 500, 'M': 1000}
    number = 0
    prev = 0
    for sym in reversed(a):
        val = roman_numbers.get(sym, 0)
        if val < prev:
            number -= val
        else:
            number += val
        prev = val
    return number

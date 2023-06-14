#!/usr/bin/python3
def roman_to_int(roman_string):
    a = roman_string[:]
    if (not isinstance(a, str) or
            a is None):
        return (0)
    roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
    num = 0
    for i in range(len(a)):
        if roman_dict.get(a[i], 0) == 0:
            return (0)
        if (i != (len(a) - 1) and
                roman_dict[a[i]] < roman_dict[a[i + 1]]):
            num += roman_dict[a[i]] * -1
        else:
            num += roman_dict[a[i]]
    return (num)

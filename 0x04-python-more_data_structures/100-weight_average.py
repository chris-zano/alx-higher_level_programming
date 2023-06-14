#!/usr/bin/python3
def weight_average(my_list=[]):
    b = my_list[:]
    a = float(sum(n for n in [x * y for x, y in b]) / sum(y for x, y in b))
    return a if my_list else 0.0


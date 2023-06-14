#!/usr/bin/python3
def weight_average(my_list=[]):
    average = 0
    result = [x * y for x, y in my_list]
    for n in result:
        average += n
    return average

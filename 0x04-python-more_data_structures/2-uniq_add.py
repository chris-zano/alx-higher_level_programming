#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list[:])
    total = 0
    for n in new_set:
        total = total + int(n)
    return total

#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    return list(map((lambda n: replace if n == search else n), new_list))

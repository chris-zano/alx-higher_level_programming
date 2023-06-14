#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sk = sorted(a_dictionary.keys())
    for k in sk:
        print(f"{k} : {a_dictionary[k]}")

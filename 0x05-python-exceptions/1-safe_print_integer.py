#!/usr/bin/python3
def safe_print_integer(value):
    istrue = True
    try:
        print("{:d}".format(value))
    except ValueError:
        istrue = False
    return istrue

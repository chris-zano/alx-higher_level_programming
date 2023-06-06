#!/usr/bin/python3
def print_tEbaHpLa():
    for c in range(ord('z'), ord('a'), -2):
        print("{:c}{:s}".format(c, uppercase(chr(c - 1))), end='')
    return


def uppercase(c):
    return chr(ord(c) - ord('a') + ord('A'))


print_tEbaHpLa()

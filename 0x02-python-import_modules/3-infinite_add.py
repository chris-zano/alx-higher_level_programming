#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv[1:]

    def add(x, sum=0):
        return sum + x

    if len(args) == 0:
        x = 0
        print("{:d}".format(x))
    elif len(args) >= 1:
        sum = 0
        for n in args:
            x = int(n)
            sum = add(x, sum)
        print("{:d}".format(sum))

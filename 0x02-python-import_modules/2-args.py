#!/usr/bin/python3
import sys
if __name__ == '__main__':
    args = sys.argv[1:]

    def print_args(args):
        for arg in range(len(args)):
            print("{:d}: {:s}".format(arg + 1, args[arg]))
        return

    if len(args) < 1:
        n = 0
        print("{:d} arguments.".format(n))
    elif len(args) == 1:
        n = 1
        print("{:d} argument:".format(n))
        print_args(args)
    elif len(args) > 1:
        n = len(args)
        print("{:d} arguments:".format(n))
        print_args(args)

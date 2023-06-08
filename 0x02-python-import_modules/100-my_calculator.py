#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys
operator = {'+': add, '-': sub, '*': mul, '/': div}
if __name__ == '__main__':
    def check_operator(str):
        state = False
        for op, cb in operator.copy().items():
            if str == op:
                state = True
                break
        return state

    args = sys.argv[1:]
    if len(args) != 3:
        print("Usage: {:s} <a> <operator> <b>".format(sys.argv[0]))
        sys.exit(1)
    elif len(args) == 3:
        if check_operator(args[1]) == False:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            for op, cb in operator.copy().items():
                if args[1] == op:
                    print("{:d} {:s} {:d} = {:d}"
                          .format(int(args[0]), args[1], int(args[2]),
                           cb(int(args[0]), int(args[2]))))


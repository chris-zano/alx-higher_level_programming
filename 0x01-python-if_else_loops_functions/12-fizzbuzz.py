#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 100):
        if i % 3 == 0:
            n = 'Fizz'
            print("{:s}".format(n), end=' ')
        elif i % 5 == 0:
            n = 'Buzz'
            print("{:s}".format(n), end=' ')
        else:
            print("{:d}".format(i), end=' ')
    if (i + 1) % 3 == 0:
        n = 'Fizz'
        print("{:s}".format(n))
    elif (i + 1) % 5 == 0:
        n = 'Buzz'
        print("{:s}".format(n))
    else:
        print("{:d}".format(i))
fizzbuzz()

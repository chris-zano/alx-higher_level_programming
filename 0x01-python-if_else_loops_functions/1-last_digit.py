#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n = int(str(abs(number))[-1])
if n > 5:
    check = 'and is greater than 5'
elif n == 0:
    check = 'and is 0'
elif n <= 5 and n != 0:
    check = 'and is less than 6 and not 0'
print(f"Last digit of {number} is {n} {check}")

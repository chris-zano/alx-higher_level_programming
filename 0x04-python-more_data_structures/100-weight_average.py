#!/usr/bin/python3
def weight_average(my_list=[]):
    b = my_list[:]
    return float(sum(n for n in [x * y for x, y in b]) / sum(y for x, y in b))

my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
# = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
result = weight_average(my_list)
print("Average: {:0.2f}".format(result))

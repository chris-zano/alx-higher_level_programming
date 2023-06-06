#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if c == ord('e') or c == ord('q'):
        pass
    else:
        print("{:c}".format(c), end="")

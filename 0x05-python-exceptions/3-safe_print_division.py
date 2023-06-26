#!/usr/bin/python3
def safe_print_division(a, b):
    q = 0
    try:
        q = a / b
    except (ZeroDivisionError, ValueError, TypeError):
        return None
    else:
        return q
    finally:
        print("Inside result: {}".format(q))

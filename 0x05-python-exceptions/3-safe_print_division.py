#!/usr/bin/python3

def safe_print_division(a, b):
    """divides 2 integers and prints the result"""

    try:
        divis = a / b
    except (TypeError, ZeroDivisionError):
        divis = None
    finally:
        print("Inside result: {}".format(divis))
    return (divis)

#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    mult = []
    for j in range(len(my_list)):
        if my_list[j] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)
    return (mult)

#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """print x elements of a list"""

    r = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            r += 1
        except IndexError:
            break
    print("")
    return (r)

#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """ function that returns a new dictionary with all values
    multiplied by 2"""

    my_dir = a_dictionary.copy()
    my_key_list = list(my_dir.keys())

    for i in my_key_list:
        my_dir[i] *= 2

    return (my_dir)

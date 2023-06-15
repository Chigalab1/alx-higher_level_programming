#!/usr/bin/python3


def print_sorted_dictionary(a_dictionary):

    dic_ord = list(a_dictionary.keys())
    dic_ord.sort()

    for i in dic_ord:
        print("{}: {}".format(i, a_dictionary.get(i)))

#!/usr/bin/python3

"""Adds 2 tuples"""


def add_tuple(tuple_a=(), tuple_b=()):

    first_comp = ""
    second_comp = ""

    tuple_a += (0, 0)
    tuple_b += (0, 0)

    first_comp = tuple_a[0] + tuple_b[0]
    second_comp = tuple_a[1] + tuple_b[1]

    return (first_comp, second_comp)

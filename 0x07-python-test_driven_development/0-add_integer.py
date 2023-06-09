#!/usr/bin/python3
# 0-add_integer.py
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """a function that adds 2 integers.
    """

    if type(a) not in (int, float):
        raise TypeError("a must be an integer")

    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    result = int(a) + int(b)
    return (result)

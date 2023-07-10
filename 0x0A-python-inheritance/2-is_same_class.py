#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """function that Check if object is exactly an instance of
    the specified class

    Returns:
        If obj is exactly an instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

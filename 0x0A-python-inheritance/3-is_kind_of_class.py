#!/usr/bin/python3
"""Module containing is_kind_of_class method"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or an inhereted
    instance of a class
    Returns:
        True if obj is an instance or inherited instance of a_class
        Otherwise - False.
    """

    if isinstance(obj, a_class):
        return (True)
    return (False)

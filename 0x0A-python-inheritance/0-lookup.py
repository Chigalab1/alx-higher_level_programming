#!/usr/bin/python3
"""Define object attribute lookup function"""


def lookup(obj):
    """function that returns the list of available attributes and
    methods of an object"""

    attributes = dir(obj)
    return (attributes)

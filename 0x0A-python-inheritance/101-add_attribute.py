#!/usr/bin/python3
""" Module that defines an object that adds attribute to
objects"""


def add_attribute(obj, attri, value):
    """add a new attribute to an object"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attri, value)

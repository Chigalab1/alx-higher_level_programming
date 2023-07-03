#!/usr/bin/python3
""" class that defines a rectangle
"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """ initialize a new Rectangle"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get/set the width of the
        rectangle"""
        return self.__width

    @property
    def height(self):
        """get/set the height of the
        width"""
        return self.__height

    @width.setter
    def width(self, value):
        """ set width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ set height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

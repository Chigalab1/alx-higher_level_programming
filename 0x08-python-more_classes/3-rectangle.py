#!/usr/bin/python3
""" defines a rectangle """


class Rectangle:
    """ class rectangle"""

    def __init__(self, width=0, height=0):
        """ initialize the rectangle"""
        self.width = width
        self.heig = height

    @property
    def width(self):
        """width of rectangle"""
        return self.__width

    @property
    def height(self):
        """height of rectangle"""
        return self.__height

    @width.setter
    def width(self, value):
        """set width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """set height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >=0")
        self.__height = value

    def area(self):
        """returns the area of
        a rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of a rectangle
        """
        if self.__width is 0 or self.__height is 0:
            return 0
        return self.__width * 2 + self.__height * 2

    def __str__(self):
        """ return the rectangle of character #
        """
        if self.__width is 0 or self.__height is 0:
            return ""

        ret = []
        for i in range(self.__height):
            for j in range(self.__width):
                ret.append('#')
            if i != self.__height - 1:
                ret.append("\n")

        return ("".join(ret))

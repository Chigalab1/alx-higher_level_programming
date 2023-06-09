#!/usr/bin/python3
"""Module that define a rectangle"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that rep a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialitse rectangle parameters"""

        self.integer_validator("height", height)
        self.__height = height

        self.integer_validator("width", width)
        self.__width = width

    def area(self):
        """Represents Area of Rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Return the print() and str() representation of a Rectangle."""
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))

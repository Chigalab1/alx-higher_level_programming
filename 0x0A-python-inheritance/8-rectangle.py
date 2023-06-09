#!/usr/bin/python3
"""DEfine Rectangle Module"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class that Represent a rectangle using BaseGeometry."""
    def __init__(self, width, height):
        """Initialitse rectangle parameters"""

        self.integer_validator("height", height)
        self.__height = height

        self.integer_validator("width", width)
        self.__width = width

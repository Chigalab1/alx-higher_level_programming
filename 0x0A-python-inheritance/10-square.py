#!/usr/bin/python3
"""Module of square class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size):
        """A Method for initializing a square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """A method that returns area of a square"""
        return (self.__size * self.__size)

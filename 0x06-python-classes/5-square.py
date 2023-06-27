#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Rep a square"""

    def __init__(self, size):
        """initialize a new square"""

        self.size = size
    @property
    def size(self):
        """get the current size of the square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print the square with # character"""
        for j in range(0, self.__size):
            [print("#", end="") for i in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
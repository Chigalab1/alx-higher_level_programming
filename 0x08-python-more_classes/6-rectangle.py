#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle."""

        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return (self.__width)

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)

        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """
        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        my_rect = []
        for i in range(self.__height):
            for j in range(self.__width):
                my_rect.append('#')
            if i != self.__height - 1:
                my_rect.append("\n")

        return ("".join(my_rect))

    def __repr__(self):
        """Return the string representation of the Rectangle."""

        my_rect = "Rectangle(" + str(self.__width)
        my_rect += ", " + str(self.__height) + ")"
        return (my_rect)

    def __del__(self):
        """ Decrements the number_of_instances class attribute and
        prints a farewell message."""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

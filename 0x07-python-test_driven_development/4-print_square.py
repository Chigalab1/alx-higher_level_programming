#!/usr/bin/python3
# 4-print_square.py
"""Defines a square-printing function."""


def print_square(size):
    """Print a square with the # character.

    Args:
        size (int): The height/width of the square.
    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """
    if not isinstance(size, int):
        raise TypeError("Invalid input. Size must be an integer.")

    # Check if size is non-negative
    if size < 0:
        raise ValueError("Invalid input. Size must be greater than or equal to 0.")

    # Print the square
    for _ in range(size):
        print("#" * size)

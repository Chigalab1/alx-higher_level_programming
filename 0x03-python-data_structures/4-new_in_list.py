#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position
    without modifying the original list."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)

    duplicate_list = [x for x in my_list]
    duplicate_list[idx] = element
    return (duplicate_list)

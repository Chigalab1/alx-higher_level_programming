#!/usr/bin/python3
# 101-remove_char_at.py
def remove_char_at(str, n):
    """func that Create a copy of the string without the character
    at position n."""
    if n < 0:
        return (str)
    return (str[:n] + str[n+1:])

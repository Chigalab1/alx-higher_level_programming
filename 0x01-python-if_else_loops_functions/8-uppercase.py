#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    """function that Print a string in uppercase."""
    edited_char = ""
    for i in str:
        if ord(i) >= 97 and ord(i) <= 122:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")

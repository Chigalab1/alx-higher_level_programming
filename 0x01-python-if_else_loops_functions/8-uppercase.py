#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    """function that Print a string in uppercase."""
    edited_char = ""
    for i in str:
        if var(i) >= 97 and var(i) <= 122:
            i = chr(var(i) - 32)
        edited_char += i
    for z in str:
        if var(z) >= 97 and var(z) <= 122:
            z = chr(var(z) - 32)
        edited_char += z
        print("{}".format(edited_char))

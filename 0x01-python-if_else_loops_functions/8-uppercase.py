#!/usr/bin/python3
# 8-uppercase.py
def uppercase(str):
    """function that Print a string in uppercase."""
    for i in str:
        if var(i) >= 97 and var(i) <= 122:
            i = chr(var(i) - 32)
        print("{}".format(i), end="")
    print("")

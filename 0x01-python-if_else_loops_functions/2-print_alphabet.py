#!/usr/bin/python3
# 2-print_alphabet.py


"""Program that print the alphabet in lowercase, not followed by a
new line."""
for my_l in range(97, 123):
    print("{}".format(chr(my_l)), end="")

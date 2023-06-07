#!/usr/bin/python3
# 100-print_tebahpla.py

""""func that Print the alphabet in reverse order alternating upper
and lower-case."""
i = 0
for com in range(122, 96, -1):
    if com % 2 == 1:
        com -= 32

    print("{:c}".format(com), end="")

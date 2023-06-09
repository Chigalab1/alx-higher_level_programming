#!/usr/bin/python3

if __name__ == "__main__":
    """Print the number of and list the arguments."""

    import sys

    my_count = len(sys.argv) - 1
    if my_count == 0:
        print("0 arguments.")

    elif my_count == 1:
        print("1 argument:")

    else:
        print("{} arguments:".format(my_count))

    for i in range(my_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
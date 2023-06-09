#!/usr/bin/python3

if __name__ == "__main__":
    """Print the sum of all arguments."""
    import sys

    my_total = 0
    for i in range(len(sys.argv) - 1):
        my_total += int(sys.argv[i + 1])
    print("{}".format(my_total))

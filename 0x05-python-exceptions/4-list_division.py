#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    """divides two integers and print the result"""

    my_list = []
    for i in range(0, list_length):
        try:
            divis = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            divis = 0
        except ZeroDivisionError:
            print("division by 0")
            divis = 0
        except IndexError:
            print("out of range")
            divis = 0
        finally:
            my_list.append(divis)
        return (my_list)

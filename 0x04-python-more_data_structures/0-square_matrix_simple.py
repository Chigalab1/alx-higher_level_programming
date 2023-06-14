#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_mat = []

    for row in matrix:
        new_row = [n**2 for n in row]

        new_mat.append(new_row)

    return (new_mat)

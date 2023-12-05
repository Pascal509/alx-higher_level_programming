#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        for i in arr:
            print("{:d}".format(i), end=" ")
        print()

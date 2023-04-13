#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        b = 1
        for c in i:
            if b < len(i):
                print("{:d}".format(c), end=" ")
            else:
                print("{:d}".format(c))
            b += 1

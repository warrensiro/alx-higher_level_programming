#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = [[i**2 for i in x] for x in matrix]
    return new_matrix

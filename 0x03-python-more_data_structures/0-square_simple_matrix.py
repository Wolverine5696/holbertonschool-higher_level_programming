#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_square = []
    for r in matrix:
        matrix_square.append(list(map(lambda x: x * x, r)))
    return (matrix_square)
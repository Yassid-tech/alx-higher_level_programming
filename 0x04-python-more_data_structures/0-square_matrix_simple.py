#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    # Use list comprehension to create a new matrix with squared values
    result_matrix = [[x**2 for x in row] for row in matrix]

    return result_matrix

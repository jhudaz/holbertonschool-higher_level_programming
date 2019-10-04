#!/usr/bin/python3

""" module "matrix"
matrix module supplies one function, matrix_divided().  For example,
>>> matrix_divided([[1,2,3],[4,5,6]], 3)
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
"""


def matrix_divided(matrix, div):
    """
    matrix_divided - divide every element in a  matrix by a divider
    """
    typeError1 = 'matrix must be a matrix (list of lists) of integers/floats'
    typeError2 = 'Each row of the matrix must have the same size'
    typeError3 = 'div must be a number'
    zeroDivision = 'division by zero'

    """" very if every element in the matrix is a list to take the length"""
    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(typeError1)
        else:
            rowLength = len(matrix[0])

    """" handle exceptions """
    if not isinstance(div, (int, float)):
        raise TypeError(typeError3)
    if div == 0:
        raise ZeroDivisionError(zeroDivision)
    if not isinstance(matrix, list):
        raise TypeError(typeError1)
    if len(matrix) == 0 or matrix == []:
        raise TypeError(typeError1)
    if matrix is None:
        raise TypeError(typeError1)

    for i in matrix:
        if not isinstance(i, list):
            raise TypeError(typeError1)
        if len(i) == 0:
            raise TypeError(typeError1)
        if len(i) != rowLength:
            raise TypeError(typeError2)
        for j in i:
            if not isinstance(j, (int, float)):
                raise TypeError(typeError1)

    """ create the new matrix"""
    return list(map(
        lambda row: list(map(
            lambda pos: round(pos / div, 2), row)), matrix))

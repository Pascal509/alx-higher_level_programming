#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a given number.

    Parameters:
    - matrix (list of lists): Matrix containing integers or floats.
    - div (number): The number to divide the matrix elements by.

    Returns:
    - list of lists: New matrix with elements divided by div, rounded to 2 decimal places.
    """
    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(elem, (int, float)) for elem in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    # Check if each row of the matrix has the same size
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return result_matrix

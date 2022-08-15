#!/usr/bin/python3


"""Define a matrix division function"""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix.
    Args:
        matrix(list): A list of lists of int/floats.
        div(int/float): The divisor.
    Raises:
        TypeError:if the matrix contains non number,
                  if the matrix contains rows of different sizes,
                  if div is not int or float
       ZeroDivisionError: if div is 0.
    Returns:
       A new matrix with the result of the division
    """
    # Checks if matrix is a list
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of lists) of "
                        "integers/floats")

    # Checks if the first element in matrix is a list so len can be used
    if isinstance(matrix[0], list):
        rowlen = len(matrix[0])

    # Checking if matrix is formatted correctly
    for item in matrix:

        # Checks if item is a list
        if not isinstance(item, list):
            raise TypeError("matrix must be a matrix (list of lists) of "
                            "integers/floats")

        # Checks if the length of each row is the same
        if len(item) != rowlen:
            raise TypeError("Each row of the matrix must have the same size")

        # Checks if the elements in the matrix are int or float
        for element in item:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of "
                                "integers/floats")

    # Checks if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Checks if div is 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    # Dividing original matrix and creating a new matrix
    new_matrix = [[round(idx / div, 2) for idx in item] for item in matrix]

    return new_matrix

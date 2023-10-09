#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for Row in matrix:
        for Column in row:
            print("{:d}".format(Column), end=" " if col != row[-1] else "")
        print("\n")


#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for Row in matrix:
        for Column in Row:
            print("{:d}".format(Column), end=" " if Column != Row[-1] else "")
        print()

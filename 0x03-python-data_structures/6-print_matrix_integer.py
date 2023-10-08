#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        print("Invalid matrix dimensions")
        return
    for i in range(3):
        for j in range(3):
            print("{:d}".format(matrix[i][j]), end=" ")
        print("\n")

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:3d}".format(col), end=" ")
        print()

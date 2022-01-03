#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        for i in range(len(line)):
            if i:
                print(end=" ")
            print(end="{:d}".format(line[i]))
        print("")

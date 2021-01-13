#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print()
    for tab in matrix:
        for nbr in range(len(tab)):
            if nbr == len(tab) - 1:
                print("{:d}".format(tab[nbr]))
            else:
                print("{:d}".format(tab[nbr]), end=" ")

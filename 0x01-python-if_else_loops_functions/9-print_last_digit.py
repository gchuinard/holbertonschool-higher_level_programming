#!/usr/bin/python3
def print_last_digit(number):
    if number > 9 and number < -9:
        nbr = number if number > 0 else -number
    else:
        nbr = number % 10 if number >= 0 else -number % 10
    print("{:d}".format(nbr), end="")
    return (nbr)

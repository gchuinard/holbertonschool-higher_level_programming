#!/usr/bin/python3
def print_last_digit(number):
    if number > 9 or number < -9:
        print("{:d}".format(number % 10 if number > 0 else -number % 10), end="")
    else:
        print("{:d}".format(number if number >= 0 else - number), end="")
    print_last_digit(98)

#!/usr/bin/python3
from calculator_1 import *


def calculator():
    import sys

    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if sys.argv[2] == '+':
        resu = add(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '-':
        resu = sub(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '*':
        resu = mul(int(sys.argv[1]), int(sys.argv[3]))
    elif sys.argv[2] == '/':
        resu = div(int(sys.argv[1]), int(sys.argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(sys.argv[1], sys.argv[2], sys.argv[3], resu))
if __name__ == "__main__":
    calculator()

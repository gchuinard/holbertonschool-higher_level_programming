#!/usr/bin/python3
def print_arg():
    import sys

    if len(sys.argv) == 1:
        print("0 arguments.")
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for i in range(len(sys.argv) - 1):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))

if __name__ == "__main__":
    print_arg()

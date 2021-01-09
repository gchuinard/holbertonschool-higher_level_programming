#!/usr/bin/python3
def add_arg():
    import sys

    nbr = 0
    if len(sys.argv) > 1:
        for i in range(len(sys.argv) - 1):
            nbr += int(sys.argv[i + 1])
    print("{:d}".format(nbr))

if __name__ == "__main__":
    add_arg()

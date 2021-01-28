#!/usr/bin/python3
"""
open a file in Python
"""


def read_file(filename=""):
    """
    reads a text file (UTF8) and prints it to stdout
    """

    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
#!/usr/bin/python3
"""
class Student
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file, after each line
    containing a specific string
    """

    result = ""
    with open(filename, 'r+') as f:
        for line in f:
            result += line
            if search_string in line:
                result += new_string
        f.close()
        with open(filename, 'w') as f:
            f.write(result)
            f.close()

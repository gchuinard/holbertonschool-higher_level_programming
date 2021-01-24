#!/usr/bin/python3
"""
text_indentation - function that prints a text with 2 new lines
                    after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    args:
        text (str): the text.
    """

    tab = ".,?:"
    line = ""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        line += char
        if char in tab:
            print(line.strip())
            print()
            line = ""
    print(line.strip(), end="")

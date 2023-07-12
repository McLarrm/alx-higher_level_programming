#!/usr/bin/python3
""" Appends a string """


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as file:
        chars_added = file.write(text)
    return chars_added

#!/usr/bin/python3
""" Writes a string to a text file """


def write_file(filename="", text=""):
    """
    Writes a string to a text file (UTF-8) and returns
    the number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as file:
        chars_written = file.write(text)
    return chars_written

#!/usr/bin/python3
""" Reads a text file """


def read_file(filename=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout
    """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")

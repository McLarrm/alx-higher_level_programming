#!/usr/bin/python3
""" Function that prints a text with 2 new lines after each character """

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = [".", "?", ":"]
    lines = text.splitlines()

    for line in lines:
        line = line.strip()
        if line:
            for char in punctuation:
                line = line.replace(char, f"{char}\n\n")
            print(line)

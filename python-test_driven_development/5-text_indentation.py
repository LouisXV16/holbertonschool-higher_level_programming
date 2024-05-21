#!/usr/bin/python3

"""function that print a text with 2 new lines after each of these charcters: . , ? , :"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Parameters:
    text: The text to be printed, must be a string.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']
    result = ''
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in characters:
            result += "\n\n"
            # Skip following spaces
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
    print(result.strip())


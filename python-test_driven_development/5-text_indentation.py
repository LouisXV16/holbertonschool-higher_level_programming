#!/usr/bin/python3

"""print a text with 2 new lines after each of these charcters: . , ? , :"""


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

    for ponctuation in ".?:":
        text = (ponctuation + "\n\n").join(
                [line.strip(" ") for line in text.split(ponctuation)])

    print("{}".format(text),end="")

#!/usr/bin/python3


""" Function that adds 2 integers """


def add_integer(a, b=98):

    """
    Args :
    a (int or float): first integer
    b (int of float): second integer
    Returns :
        integer: addition of a and b
    Raises :
        TypeError: if a or b is not an integer or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

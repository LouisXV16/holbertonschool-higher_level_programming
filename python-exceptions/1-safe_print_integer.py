#!/usr/bin/python3
def safe_print_integer(value):
    """
    Attempts to print an integer value.

    Args:
        value: The value to be printed. This can be any type.

    Returns:
        bool: True if the value was successfully printed as an integer, False otherwise.
    """
    try:
        # Attempt to format and print the value as an integer
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        # If a ValueError or TypeError is raised, the function returns False
        return False

#!/usr/bin/python3
"""
9-rectangle.py

This module defines a Rectangle class that inherits from BaseGeometry.
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    The 'Rectangle' class inherits from 'BaseGeometry'.
    """

    def __init__(self, width, height):
        """
        Initializes the Rectangle with width and height,
        validated by BaseGeometry.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the rectangle.

        Returns:
            str: The string representation of the rectangle.
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

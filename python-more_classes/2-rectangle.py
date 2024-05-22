#!/usr/bin/python3

""" Class Rectangle that defines a rectangle"""


class Rectangle:
    """
    Definces a rectangle by width and height
    Attributes:
        width (int): width of the rectangle
        height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initializes a rectangle instance
        Args:
            widht (int, optional): width of the rectangle
            height (int, optional): height of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Getter method for width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for widht attribute
        Args:
            value (int): width of the rectangle
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Getter method for height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter method  of height attribute
        Args:
            value (int): height of the rectangle
        Raises:
            TypeError: if value is not an int
            ValueError: if value is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Returns area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Returns perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

#!/usr/bin/python3
# 0-square.py
"""x."""


class Square:
    def __init__(self, size=0):
        """
        x
        """
        self.size = size  # uses the setter for validation

    @property
    def size(self):
        """
        x
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        x
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        x
        """
        return self.__size ** 2
    

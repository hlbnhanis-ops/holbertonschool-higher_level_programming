#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        x
        """
        self.size = size

    def size(self):
        """
        x
        """
        return self.__size

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
        return self.__size ** 2;

    def my_print(self):
        """
        x
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__size):
            print("#" * self.__size)

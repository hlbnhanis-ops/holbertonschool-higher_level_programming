#!/usr/bin/python3

class Square:
    def __init__(self, size=0, position=(0, 0)):
        """
        x
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        x
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        x
        """
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(i, int) for i in value) or
            not all(i >= 0 for i in value)
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        x
        """
        return self.__size ** 2

    def my_print(self):
        """
        x
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")

        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

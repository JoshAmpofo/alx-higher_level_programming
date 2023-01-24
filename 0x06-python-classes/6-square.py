#!/usr/bin/python3
"""Module that defines a class Square"""


class Square:
    """create an instance of the class Square"""

    def __init__(self, size=0, position=(0, 0)):
        """Initiliaze and validate attribute of the class Square.

        Args:
        __size (int): private instance of the class Square.
        Determines the size of the class Square.
        __position (int, int): private instance of the class Square.
        Determines the coordinates of the class Square
        """
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """int: get the size of the class Square"""
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """int, int: get the coordinates of the class Square"""
        return self.__position

    @position.setter
    def position(self, value):
        if not (isinstance(value, tuple) and len(value) == 2
                and all(isinstance(i, int)
                        and i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """method returns square of current area"""
        return self.__size ** 2

    def my_print(self):
        """method prints square with # to stdout"""
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(self.__position[1])]

        for i in range(self.__size):
            [print(" ", end="") for j in range(self.__position[0])]
            [print("#", end="") for k in range(self.__size)]
            print("")

#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """initialization method"""
    def __init__(self, size=0):
        """validate size as int"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """method to compute area"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter decorator"""
        return '{}'.format(self.__size)

    @size.setter
    def size(self, value):
        """setter decorator"""
        self.__size = value

    def my_print(self):
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print()

#!/usr/bin/python3
"""class that defines a square"""


class Square:
    """initialization method"""
    def __int__(self, size=0):
        """validate size as int"""
        if not type(size) is int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    def area(self):
        """method to compute area"""
        return size.__size * self.__size

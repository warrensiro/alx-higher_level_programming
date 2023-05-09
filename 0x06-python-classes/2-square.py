#!/usr/bin/python3
"""Class that defines a square"""
class Square:
    """initialization method"""
    def __init__(self, size=0):
        """checking type of size"""
        """continue with execution if an integer else raise the exception"""
        if not type(size) is int:
            """Exception raised"""
            raise TypeError("size must be an integer")
        """continue if size is positive"""
        elif size < 0:
            """Exception raised"""
            raise ValueError("size must be >= 0")
        """Assign the positive integer to a private instance attribute size"""
        else:
            self.__size = size

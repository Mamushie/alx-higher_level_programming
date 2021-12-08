#!/usr/bin/python3
"""Defining a Class called Square"""


class Square:
    """Attributes of the class Square defined"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Return: size"""
        return self.__size

    @size.setter
    def size(size, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current area of the square"""
        return (self.__size * self__size)

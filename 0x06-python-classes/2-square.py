#!/usr/bin/python3
class Square:
    """A class that represents a square."""

    def _init_(self, size=0):
        """Initialize the square with the given size."""
        self.__size = size # private instance attribute
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

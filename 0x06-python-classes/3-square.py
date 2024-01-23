#!/usr/bin/python3
"""Introduces a class named Square."""


class Square:
    """A class defining the properties of a square,
    as specified in 2-square.py.

    Attributes:
    size: The size of the square,
    representing the length of one side.
    """
    def __init__(self, size=0):
        """Generates new instances of a square.

        Args:
            size: The size of the square,
            representing the length of one side.
        """
        self.__size = size

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns: The current are of the square.
        """
        return self.__size ** 2

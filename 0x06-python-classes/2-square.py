#!/usr/bin/python3
"""Introduces a class named Square."""


class Square:
    """A class that specifies the properties of a square,
    following the specifications outlined in 1-square.py.

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

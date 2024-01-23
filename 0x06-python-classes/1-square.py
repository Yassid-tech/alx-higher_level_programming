#!/usr/bin/python3
"""Defines a class Square"""


class Square:
    """A class defining the properties of a square,
    specifically based on the characteristics outlined
    in 0-square.py

    Attributes:
    size: The size of the square.
    """
    def __init__(self, size):
        """Generates new instances of a square,
        each with a specified size.

        Args:
        size: The size of the square.
        """
        self.__size = size

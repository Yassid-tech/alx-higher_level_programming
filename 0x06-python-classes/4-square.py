#!/usr/bin/python3
"""Introduces a class named Square."""


class Square:
    """
    A class defining the properties of a square,
    following the specifications outlined in 3-square.py.

    Attributes:
        size: size of a square,
        representing the length of one side.
    """

    def __init__(self, size=0):
        """Creates new instances of a square.

        Args:
            size: The size of the square,
            representing the length of one side.
        """
        self.__size = size

    def area(self):
        """Calculates the area of the square.

        Returns: the current area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter for size.

        Args:
            value (int): The size of the square,
            representing the length of one side.

        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than 0
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

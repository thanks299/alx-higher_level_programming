#!//usr/bin/python3


class Square:
    """A class representing a square with a private instance attribute 'size'."""

    def __init__(self, size=0):
        """
        Initialize a new Square object with a given size.

        :param size: The size of the square.
        """
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        :return: The area of the square.
        """
        return self.__size ** 2

    def __str__(self):
        """
        Return a string representation of the square.

        :return: A string representation of the square.
        """
        return "#" * self.__size

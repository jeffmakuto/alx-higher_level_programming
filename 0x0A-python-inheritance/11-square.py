#!/usr/bin/python3
"""
Defines a Square class that inherits from Rectangle (9-rectangle.py).
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """
    Represents a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.
        Args:
            size (int): The size of the square's sides.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns a string representation of the square.
        """
        return "[Square] {}/{}".format(self.__width, self.__height)

if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())


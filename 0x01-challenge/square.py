#!/usr/bin/python3
"""
Module generates square.
"""

class square():
    """
    Create empty class square.
    """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """
        Initialization.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """Correction: Area of the square """
        return self.width * self.height

    def PermiterOfMySquare(self):
        """
        Function calculates perimeter.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Function handles string representation.
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

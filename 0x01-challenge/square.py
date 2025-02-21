#!/usr/bin/python3
"""
Module generates square.
"""


class Square():
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
        """
        Function returns area of square.
        """
        return self.width * self.height

    def Permiter_Of_My_Square(self):
        """
        Function returns perimeter of square.
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Function handles string representation.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.Permiter_Of_My_Square())

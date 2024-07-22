#!/usr/bin/python3

class square():

    width = 0
    height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def is_perfect_square(self):
        """Check if the shape is a perfect square"""
        return self.width == self.height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":

    s = square(width=12, height=12)
    print(s)
    print(s.is_perfect_square())
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())

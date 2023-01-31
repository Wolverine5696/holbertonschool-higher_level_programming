#!/usr/bin/python3
"""
BaseGeometry is the main class and Rectangle and Square is the subclass
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
    def area(self):
        return self.__size ** 2
    
    def __str__(self):
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

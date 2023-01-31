#!/usr/bin/python3
"""
class Basegeometry and Subclass is Rectangle
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle subclass
    """
    
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """This function is the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """This function returns a description about this class"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

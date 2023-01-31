#!/usr/bin/python3
"""
Class BaseGeometry
"""


class BaseGeometry:
    """public area class"""
    
    def area(self):
        """Raises: exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Raises TypeError if its not an integer
        ValueError if its <=0
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

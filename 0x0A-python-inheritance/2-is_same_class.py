#!/usr/bin/python3
"""
Write a function that returns true if the object is an
instance of the specified class, otherwise  returns false.
        *Prototype: def is_same_class(obj, a_class):
"""


def is_same_class(obj, a_class):
    """This function is true if the object is an instance of the
       specified class"""
    return type(obj) is a_class

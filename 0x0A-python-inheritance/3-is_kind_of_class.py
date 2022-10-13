#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class ; otherwise returns false.
"""


def is_kind_of_class(obj, a_class):
    """ This function returns true if the object is a instance of, if the
        object is an instance of a class that  it
        inherited from"""
    return isinstance(obj, a_class)

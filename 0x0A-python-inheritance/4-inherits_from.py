#!/usr/bin/python3
"""
Write a function that returns True if the object is an instance of a class
that inherited (directly or indirectly) from the specified class ;
otherwise False.
"""


def inherits_from(obj, a_class):
    """ Return true if the object is a instance of a class that inherited from
        the specified class.
    """    
    if type(obj) == a_class:
        return False
    return (issubclass(type(obj), a_class))

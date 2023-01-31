#!/usr/bin/python3
"""
my list class that inherits from a list
"""


class mylist(list):
    """Public instance method that prints the list, but sorted (ascending sort)"""
    def __init__(self):
        """initializes the object using the super()"""
        super().__init__()
        
    def print_sorted(self):
        """prints itself sorted"""
        print(sorted(self))
     

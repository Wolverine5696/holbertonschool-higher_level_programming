#!/usr/bin/python3
"""
my list class that inherits from a list
"""


class mylist(list):
    """Public instance method that prints the list, but sorted (ascending sort)"""
    def print_sorted(self):
        print(sorted(self))
     

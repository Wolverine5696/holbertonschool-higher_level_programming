
#!/usr/bin/python3
"""
This is the function for 4-print_square.py
"""


def print_square(size):
    """This function prints a square with the character #, size >= 0"""
    if isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)

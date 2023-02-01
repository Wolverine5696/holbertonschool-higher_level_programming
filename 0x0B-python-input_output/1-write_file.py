#!/usr/bin/python3
""" Function that writes in a text file """

def write_file(filename="", text=""):
    """ Function writes a File and Returns the number of characters written """
    with open(filename, mode="w", encoding="utf-8") as theFilename:
        contents = theFilename.write(text)
    return contents

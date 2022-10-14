#!/usr/bin/python3
""" Function That appends a string at the end the a Text File """


def append_write(filename="", text=""):
    """ Function that appends a string at the end of the file and returns the
    the number of characters added """
    with open(filename, mode="a", encoding='utf-8') as theFilename:
        contents = theFilename.write(text)
    return contents

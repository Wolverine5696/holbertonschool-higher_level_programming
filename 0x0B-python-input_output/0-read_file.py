#!/usr/bin/python3
""" Defines A Function That Reads a text File """


def read_file(filename=""):
    """ function that reads the file and prints the text"""
    with open(filename, mode="r", encoding='utf-8') as theFilename:
        contents = theFilename.read()
        print(contents, end="")

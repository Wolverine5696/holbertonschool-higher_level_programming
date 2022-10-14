#!/usr/bin/python3
"""function that returns an object /"""
import json


def save_to_json_file(my_obj, filename):
    """function that returns an object (Python data structure)
    represented by a JSON string:"""
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)

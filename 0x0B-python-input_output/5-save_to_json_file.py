#!/usr/bin/python3
""" Module for save_to_json_file method
"""
import json


def save_to_json_file(my_obj, filename):
    """ write an object to a json file

    Args:
        my_obj (str): object to be written
        filename (str): filename/path
    """
    with open(filename, mode="w") as file:
        json.dump(my_obj, file)

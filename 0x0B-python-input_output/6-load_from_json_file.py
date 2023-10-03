#!/usr/bin/python3
""" Module for load_from_json_file method
"""
import json


def load_from_json_file(filename):
    """ load json file to a python object

    Args:
        filename (str): filename/path
    """
    with open(filename) as file:
        return (json.load(file))

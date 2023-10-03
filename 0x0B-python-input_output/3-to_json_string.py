#!/usr/bin/python3
""" Module for to_json_string method
"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)

    Args:
        my_obj (str): string to be converted
    """
    return json.dumps(my_obj)

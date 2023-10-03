#!/usr/bin/python3
""" Module for from_json_string method
"""
import json


def from_json_string(my_str):
    """Returns an object (Python data structure) represented by a JSON string

    Args:
        my_str (str): json string
    """
    return json.loads(my_str)

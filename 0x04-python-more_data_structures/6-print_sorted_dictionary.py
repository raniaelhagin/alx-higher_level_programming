#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    """Sort dictionary by keys"""

    sorted_keys = sorted(list(a_dictionary.keys()))
    sorted_dict = {key: a_dictionary[key] for key in sorted_keys}

    for key, value in sorted_dict.items():
        print("{}: {}".format(key, value))

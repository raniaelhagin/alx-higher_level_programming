#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    """ remove a key from a dictionary"""

    try:
        del a_dictionary[key]
    except KeyError:
        pass

    return (a_dictionary)

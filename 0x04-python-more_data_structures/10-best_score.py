#!/usr/bin/python3

def best_score(a_dictionary):
    """ returns a key with the biggest integer value """

    if a_dictionary:
        max_val = next(iter(a_dictionary.values()))

        for key, value in a_dictionary.items():

            if a_dictionary[key] > max_val:
                max_val = a_dictionary[key]
                targeted_key = key

        return (targeted_key)

    else:
        return (None)

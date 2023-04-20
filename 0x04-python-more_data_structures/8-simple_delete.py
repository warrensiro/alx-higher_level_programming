#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    get_key = key in a_dictionary
    if get_key is True:
        return a_dictionary.pop(key)

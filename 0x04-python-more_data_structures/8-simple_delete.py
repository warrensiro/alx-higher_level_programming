#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary == {}:
        return a_dictionary
    else:
        return a_dictionary.pop(key)

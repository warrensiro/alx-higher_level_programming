#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or a_dictionary == {}:
        return None
    biggest_value = max(a_dictionary, key=a_dictionary.get)
    return biggest_value

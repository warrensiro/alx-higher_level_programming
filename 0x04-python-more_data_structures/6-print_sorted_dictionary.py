#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict_1 = list(a_dictionary.keys())
    dict_1.sort()
    dict_1 = {i: a_dictionary[i]
    for i in dict_1}
    return dict_1

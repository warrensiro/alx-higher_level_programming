#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_1 = list(a_dictionary.keys())
    dict_1.sort()
    for i in dict_1:
        print("{:s}: {}".format(i, a_dictionary[i*2]))

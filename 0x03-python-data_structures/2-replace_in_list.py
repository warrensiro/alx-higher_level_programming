#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if (idx < 0) or (idx > len(my_list) - 1):
        continue
    i = 0
    while True:
        if i == idx:
            return element(my_list[i])

#!/usr/bin/python3
def element_at(my_list, idx):
    if (idx < 0) or (idx > (len(my_list) - 1)):
        return None
    i = 0
    while True:
        if i == idx:
            return my_list[i]
            i += 1

#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for i in sorted(set(my_list)):
        total += i
    return total

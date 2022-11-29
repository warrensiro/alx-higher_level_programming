#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        newnum = number * -1
        newnum = newnum % 10
    else:
        newnum = number % 10
    print('{:d}'.format(newnum), end="")
    return newnum

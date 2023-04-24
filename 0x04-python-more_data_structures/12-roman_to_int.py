#!/usr/bin/python3
def roman_to_int(roman_string):
    number = 0
    if roman_string == "" or roman_string is None:
        return 0
    for i in range(len(roman_string)):
        if roman_string[i] == "M":
            number += 1000
            if roman_string[i-1] == "C" and i != 0:
                number -= 100
        if roman_string[i] == "D":
            number += 500
            if roman_string[i-1] == "C" and i != 0:
                number -= 100
        if roman_string[i] == "C":
            number += 100
            if roman_string[i-1] == "X" and i != 0:
                number -= 10
        if roman_string[i] == "L":
            number += 50
            if roman_string[i-1] == "X" and i != 0:
                number -= 10
        if roman_string[i] == "X":
            number += 10
            if roman_string[i-1] == "I" and i != 0:
                number -= 1
        if roman_string[i] == "V":
            number += 5
            if roman_string[i-1] == "I" and i != 0:
                number -= 1
        if roman_string[i] == "I":
            number += 1
    return number

#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if ((number % 10) == 0):
    print(f"Last digit of {number} is {number % 10} and is 0")
while (number < 0):
    print(f"Last digit of {number} is {-(10 - (number % 10))} and is less than 6 and not 0")
    break
while (number > 0):
    if ((number % 10) > 5) and ((number % 10) != 0):
        print(f"Last digit of {number} is {number % 10} and is greater than 5")
    elif ((Number % 10) < 6) and ((number % 10) != 0):
        print(f"Last digit of {number} is {number % 10} and is less than 6 and not 0")
    break

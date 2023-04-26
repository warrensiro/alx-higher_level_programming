#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            if any(char.isdigit()):
                print("{}".format(my_list[i]), end="")
                j += 1
            print("")
            return x
        except (IndexError, TypeError) as e:
            print(e)
            return x

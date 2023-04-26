#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        result = [i/j for i, j in zip(my_list_1, my_list_2)]
    except ZeroDivisionError:
        result = 0
       print("division by 0")
    except (TypeError, ValueError):
        result = 0
        print("wrong type")
    except IndexError:
        result = 0
        print("out of range")
    finally:
        return result

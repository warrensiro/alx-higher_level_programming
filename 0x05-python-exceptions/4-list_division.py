#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    division_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
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
            division_list.append(result)
    return division_list

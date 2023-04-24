#!/usr/bin/python3
def weight_average(my_list=[]):
    prod_list, count, divider, sum_average = 1, 0, 0, 0
    if my_list == []:
        return 0
    for i in my_list:
        for j in i:
            prod_list *= j
            if count == 1:
                prod_list += j
            count += 1
        sum_average += prod_list
        prod_list, count = 1, 0
    weighted_average = sum_average / prod_list
    return weighted_average

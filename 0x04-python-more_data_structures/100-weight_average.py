#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    avg_weight = 0
    weight_size = 0

    for size, weight in my_list:
        avg_weight += weight * size
        weight_size += weight

    if avg_weight == 0:
        return 0

    return avg_weight / weight_size

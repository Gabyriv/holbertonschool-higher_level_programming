#!/usr/bin/python3

def uniq_add(my_list=[]):
    total_sum = 0
    integers_seen = []
    for i in my_list:
        if i not in integers_seen:
            total_sum += i
            integers_seen.append(i)

    return total_sum

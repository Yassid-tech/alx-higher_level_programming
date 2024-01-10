#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Use a set to keep track of unique integers
    unique_set = set()

    # Iterate through the list and add unique integers to the set
    for num in my_list:
        unique_set.add(num)

    # Calculate the sum of unique integers
    sum_unique = sum(unique_set)

    return sum_unique

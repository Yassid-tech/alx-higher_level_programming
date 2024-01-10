#!/usr/bin/python3
def search_replace(my_list, search, replace):
    # Use list comprehension to create a new list with replacements
    return [replace if element == search else element for element in my_list]

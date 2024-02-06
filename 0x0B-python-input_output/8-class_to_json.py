#!/usr/bin/python3
"""Function that returns the dictionary description
with simple data structure"""


def class_to_json(obj):
    """Module class_to_json
    returns builds a dictionary
    """
    return obj.__dict__

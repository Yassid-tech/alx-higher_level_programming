#!/usr/bin/python3
"""Function that returns the JSON representation of an object(String)"""

import json


def to_json_string(my_obj):
    """Module to_json_string
    returns JSON representation
    """
    return json.dumps(my_obj)

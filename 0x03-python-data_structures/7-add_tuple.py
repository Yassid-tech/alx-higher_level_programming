#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Ensure both tuples have at least 2 elements by padding with zeros if necessary
    padded_a = tuple_a + (0, 0) if len(tuple_a) < 2 else tuple_a[:2]
    padded_b = tuple_b + (0, 0) if len(tuple_b) < 2 else tuple_b[:2]
    
    # Perform element-wise addition and create a new tuple
    result = (padded_a[0] + padded_b[0], padded_a[1] + padded_b[1])
    return result

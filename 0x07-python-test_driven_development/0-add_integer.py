#!/usr/bin/python3

"""
0-add_integer module
"""

def add_integer(a, b=98):
    """
    check if a and b are a instance of floats and ints and assign their respective values
    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    """
    if above is not true, raise TypeError
    """
    if not isinstance(a, int):
        raise TypeError("a must be an integer")
    if not isinstance(b, int):
        raise TypeError("b must be an integer")
    return a + b

#!/usr/bin/python3
"""
Defines method is_same_class and 
returns True if object is exactly an instance of specified class
"""


def is_same_class(obj, a_class):
    """
    Notes:
        use type() to get specific class
        use isinstance() to get class and any parent classes too
        use issubclass() to get what object is a subclass of
    Return:
        True if obj is exactly an instance of specified class
    """
    return type(obj) == a_class

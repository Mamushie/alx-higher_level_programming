#!/usr/bin/python3
"""Defines a locked class module"""


class LockedClass:
    """Prevents creation of dynamic attribute"""

    __slots__ = ['first_name']

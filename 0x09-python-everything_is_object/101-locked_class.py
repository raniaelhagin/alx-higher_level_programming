#!/usr/bin/python3
"""creating a locked class"""


class LockedClass:
    """
    Prevents the user from creating new
    attributes except first_name
    """
    __slots__ = ["first_name"]

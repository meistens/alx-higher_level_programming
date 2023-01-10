#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """This class invert the operators"""
    def __eq__(self, other):
        """Overwrite to false """
        return False

    def __ne__(self, other):
        """OverWrite to true """
        return True

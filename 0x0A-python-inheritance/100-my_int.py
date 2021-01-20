#!/usr/bin/python3
""" Nasty int module
"""


class MyInt(int):
    """ makes a mean int
    """

    def __ne__(self, other):
        """ reverses !=
        """
        return super().__eq__(other)

    def __eq__(self, other):
        """ reverses ==
        """
        return super().__ne__(other)

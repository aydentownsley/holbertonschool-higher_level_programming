#!/usr/bin/python3
""" Inheritance Module """


class MyList(list):
    """
        class
    """

    def print_sorted(self):
        """
            prints sorted list
            in ascending order
        """
        print(sorted(self))

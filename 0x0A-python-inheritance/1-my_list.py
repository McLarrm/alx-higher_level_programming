#!/usr/bin/python3
""" MyList """


class MyList(list):
    """ A MyList class that inherits from list """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

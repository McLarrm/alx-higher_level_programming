#!/usr/bin/python3
""" Adds all arguments to a Python list """
import sys
from os.path import exists


def save_to_json_file(my_obj, filename):
    """ Function implementation """
def load_from_json_file(filename):

filename = "add_item.json"

if exists(filename):
    my_list = load_from_json_file(filename)
else
    my_list = []

my_list.extend(sys.argv[1:])

save_to_json_file(my_list, filename)

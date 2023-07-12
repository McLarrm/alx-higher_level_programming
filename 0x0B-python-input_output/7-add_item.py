#!/usr/bin/python3
""" Adds all arguments to a Python list """
import sys
import json
savejson = __import__("7-save_to_json_file").save_to_json_file
loadjson = __import__("8-load_from_json_file").load_from_json_file

try:
    lists = loadjson("add_item.json")
except FileNotFoundError:
    lists = []
for arg in sys.argv[1:]:
    lists.append(arg)
savejson(lists, "add_item.json")

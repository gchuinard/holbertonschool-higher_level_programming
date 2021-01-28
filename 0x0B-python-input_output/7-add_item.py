#!/usr/bin/python3
"""
adds all arguments to a Python list, and then save them to a file
"""

import sys
save_json = __import__('5-save_to_json_file').save_to_json_file
load_json = __import__('6-load_from_json_file').load_from_json_file

try:
    item = load_json("add_item.json")
except:
    item = []

item.extend(sys.argv[1:])
save_json(item, "add_item.json")

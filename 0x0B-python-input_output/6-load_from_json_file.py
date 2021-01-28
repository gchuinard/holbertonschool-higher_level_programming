#!/usr/bin/python3
"""
open a file in Python
"""

import json


def load_from_json_file(filename):
    """
    creates an Object from a “JSON file”
    """

    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)

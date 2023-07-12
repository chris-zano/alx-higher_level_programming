#!/usr/bin/python3
"""
This is the 7-add_item.py module
This module provides one method
"""


import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_item.json"
try:
    result = load_from_json_file(filename)
except Exception:
    result = []
result += sys.argv[1:]
save_to_json_file(result, filename)

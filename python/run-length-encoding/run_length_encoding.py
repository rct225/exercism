from itertools import groupby
import re

def decode(string):
    if not string:
        return ""

    if not string[0].isdigit():
        return string[0] + decode(string[1:])

    string_match = re.match(r"(\d+)(\D)", string)

    string_skip = len(string_match.group(1)) + 1
    return string_match.group(2) * int(string_match.group(1)) + decode(string[string_skip:])

def encode(string):
    encoded = ''

    for key, group in groupby(string):
        group_len = len(list(group))
        if group_len == 1:
            encoded += key
        else:
            encoded += str(group_len) + key

    return encoded

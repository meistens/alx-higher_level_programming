#!/usr/bin/python3
def remove_char_at(str, n):
    emptyStr = ""
    i = 0
    for c in str:
        if i != n:
            emptyStr += c
        i += 1
    return emptyStr

#!/usr/bin/python3
def remove_char_at(str, n):
    s = ""
    m = 0
    lon = len(str)
    if n < 0 or lon < n:
        return str
    else:
        while lon > m:
            if n == m:
                m += 1
                continue
            s += str[m]
            m += 1
        return s

# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re


def to_7(num):
    s = ""
    while num:
        s += str(num % 7)
        num //= 7
    return s[::-1]


k = 1
for i in range(333, 10**9 + 1, 333):
    t = to_7(i)
    if re.fullmatch(r"\d213\d*5664", t):
        print(i, i // 333)

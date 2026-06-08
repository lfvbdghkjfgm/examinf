# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return res


for i in range(1861, 10**10, 1861):
    if re.fullmatch(r"3\d67\d*2\d1", str(i)):
        t = dels(i)
        if t:
            m = min(t) + max(t)
            if m % 100 == 52:
                print(i, max(t))

# Solved by Данзан С.

import fnmatch


def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))


for x in range(1861, 10**10, 1861):
    if fnmatch.fnmatch(str(x), "3?67*2?1"):
        l = dels(x)
        if len(l) > 1:
            M = max(l) + min(l)
            if str(M)[-2:] == "52":
                print(x, max(l))

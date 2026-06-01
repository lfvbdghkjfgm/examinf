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

# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return res


for i in range(1945, 10**10, 1945):
    if re.fullmatch(r"6\d38\d*9\d5", str(i)):
        t = dels(i)
        if t:
            m = min(t) + max(t)
            if m % 1000 == 792:
                print(i, sum(map(int, str(m))))

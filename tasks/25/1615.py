# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re


def dels(num):
    res = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


k = 0
for i in range(int((10**9) ** 0.5) + 1, 10**9):
    i = i**2
    if re.fullmatch(r"1\d*2\d*7\d*04", str(i)):
        t = dels(i)
        if len(t) == 45:
            print(i, t[-2])
            k += 1
    if k == 5:
        break

# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from math import prod


def dels(num):
    res = set()
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


k = 0
for i in range(800001, 10**10):
    t = dels(i)
    if sum(t) % 2 != 0 and prod(t) % 2 != 0 and len(t) > 10:
        print(i, len(t))
        k += 1
    if k == 6:
        break

# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product


def from_ss(l, ss):
    res = 0
    for a, i in enumerate(l[::-1]):
        res += i * ss**a
    return res


def to_ss(num, ss):
    res = []
    while num >= ss:
        res.append(num % ss)

        num //= ss
    res.append(num)
    return res[::-1]


a = 4 * 625**1920 - 4 * 25**1940 - 3 * 5**1950 - 1960

for x in range(10_000):
    if to_ss(a + 4 * 125**x, 5).count(0) == 1891:
        print(x)
# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product


def P(x):
    return 5 <= x <= 54


def Q(x):
    return 50 <= x <= 93


for a in range(1000):
    ct = 0
    for x in range(1000):
        if (((not P(x)) and Q(x)) <= (x > a)) == 0:
            ct += 1
        if ct > 20:
            break
    if ct == 20:
        print(a)
        break

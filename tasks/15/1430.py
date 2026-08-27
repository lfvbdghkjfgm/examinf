# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

res = 0
for a in range(1, 2000):
    flag = True
    for x, y in product(range(1, 2000), repeat=2):
        if ((x % a == 0) <= ((x % 55 != 0) <= (y % 101 != 0))) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

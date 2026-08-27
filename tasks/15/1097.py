# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

for a in range(1000, 0, -1):
    flag = True
    for x, y in product(range(1000), repeat=2):
        if ((x > a) or (y > a) or (y - 2 * x + 12 != 0)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

for a in range(1000):
    flag = True
    for x, y in product(range(1, 500), repeat=2):
        if ((2 * x - 4 * y < a) or (y >= x) or (x > 67)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

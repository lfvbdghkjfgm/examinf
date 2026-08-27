# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

for a in range(1000):
    flag = True
    for x, y in product(range(1, 500), repeat=2):
        if ((x - 3 * y < a) or (y > 400) or (x > 56)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

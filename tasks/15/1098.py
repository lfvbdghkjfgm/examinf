# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(1, 5000):
    flag = True
    for x in range(1, 5000):
        if (((x % 3 == 0) <= (x % 17 != 0)) or not (a < 190 - x)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

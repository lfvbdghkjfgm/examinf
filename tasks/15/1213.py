# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(1, 5000):
    flag = True
    for x in range(1, 5000):
        if (((405 % x == 0) <= (81 % x == 0)) or (a - x > 162)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

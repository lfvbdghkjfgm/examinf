# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(5000):
    flag = True
    for x, y in product(range(1, 1000), repeat=2):
        if ((x * y > a) and (x > y) and (x < 8)) == 1:
            flag = False
            break
    if flag:
        print(a)
        break

# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(5000, 1, -1):
    flag = True
    for x, y in product(range(1, 1000), repeat=2):
        if ((9 * x + y > a) or (x >= 36) or (y >= 18)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

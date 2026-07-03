# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(5000):
    flag = True
    for x, y in product(range(1000), repeat=2):
        if ((5 < y) or (x > 32) or (x + 2 * y < a)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

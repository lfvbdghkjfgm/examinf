# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(5000, 1, -1):
    flag = True
    for x, y in product(range(1, 1000), repeat=2):
        if ((3 * y + 2 * x != 130) or (3 * x > a) or (2 * y > a)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

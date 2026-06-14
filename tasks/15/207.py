# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(500, 0, -1):
    flag = True
    for x, y in product(range(1000), repeat=2):
        if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)) == 0:
            flag = False
            break
    if not flag:
        print(a)
        break

# Solved by Аня

for a in range(0, 1000):
    can = True
    for x in range(0, 1000):
        for y in range(0, 1000):
            if ((4 * x + y > 115) or (x > 3 * y) or (x + 4 * y < a)) == 0:
                print(a)
                can = False
                break
        if can == False:
            break

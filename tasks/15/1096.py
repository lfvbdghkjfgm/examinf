# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for a in range(5000, 0, -1):
    flag = True
    for x in range(1, 5000):
        if (((x % 3 == 0) <= (x % 2 != 0)) or (x - a >= 4)) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

# Solved by Мария


for A in range(1, 100000):
    can = True
    for x in range(1, 100000):
        if (((x % 3 == 0) <= (x % 2 != 0)) or (x - A >= 4)) == 0:
            can = False
            break
    if can:
        print(A)

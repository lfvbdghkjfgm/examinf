# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

res = 0
for a in range(1, 1001):
    flag = True
    for x in range(1, 5000):
        if (
            ((a % 35 == 0) and ((730 % x == 0)) <= ((a % x != 0) <= (100 % x != 0)))
        ) == 0:
            flag = False
            break
    if flag:
        res += 1
print(res)

# Solved by Иса


m = []
for a in range(1, 1001):
    k = 0
    for x in range(1, 10001):
        if (
            (a % 35 == 0) and ((730 % x == 0) <= ((a % x != 0) <= (110 % x != 0)))
        ) == 1:
            k += 1
    if k == 10000:
        m.append(a)
print(len(m))

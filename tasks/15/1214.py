# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

for a in range(5000, 1, -1):
    flag = True
    for x in range(1, 5000):
        if ((x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0))) == 0:
            flag = False
            break
    if flag:
        print(a)
        break

# Solved by София


def f(x):
    return (x & A != 0) <= ((x & 698 == 0) <= (x & 321 != 0))


for A in range(1, 10000):
    if all(f(x) == 1 for x in range(1, 10000)):
        print(A)

# Solved by Иса


for a in range(1, 2000):
    k = 0
    for x in range(1, 10001):
        if ((x & a != 0) <= ((x & 698 == 0) <= (x & 321 != 0))) == 1:
            k += 1
    if k == 10000:
        print(a)

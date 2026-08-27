# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

res = 0
for i in product(range(16), repeat=5):
    if (
        i[0] != 0
        and all([i.count(j) <= 2 for j in i])
        and any([j in i for j in [1, 4, 9]])
    ):
        res += 1
print(res)

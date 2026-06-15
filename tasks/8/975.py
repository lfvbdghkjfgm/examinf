# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product, permutations

res = 0
for i in product(range(12), repeat=5):
    if i.count(7) == 1 and len([j for j in i if j > 8]) <= 3 and i[0] != 0:
        res += 1
print(res)

# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product, permutations

res = 0
for i in product(range(9), repeat=7):
    if i[0] != 0 and i[0] % 2 == 0 and i[-1] % 3 != 0 and 6 in i:
        res += 1
print(res)

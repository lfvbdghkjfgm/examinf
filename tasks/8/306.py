# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product, permutations

res = set()
for x in permutations("АМФИБРАХИЙ"):
    x = "".join(x)
    if x[5:7] == "БР":
        res.add(x)
print(len(res))

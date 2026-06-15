# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product, permutations

res = set()
for x in permutations("АМФИБРАХИЙ"):
    x = "".join(x)
    if x[5:7] == "БР":
        res.add(x)
print(len(res))

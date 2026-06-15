# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product, permutations

res = set()
for x in permutations("АМФИБРАХИЙ"):
    x = "".join(x)
    t = x.index("Ф")
    if 2 <= t <= len(x) - 3:
        if x[t - 2 : t] in ["АА", "ИИ"] and x[t + 1 : t + 3] in ["АА", "ИИ"]:
            res.add(x)
print(len(res))

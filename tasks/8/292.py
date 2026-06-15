# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product, permutations

res = 0
for i in product("01234567", repeat=5):
    if i[0] != "0" and i.count("3") <= 1:
        i = "".join(i)
        for j in "1357":
            i = i.replace(j, "*")
        if "**" not in i:
            res += 1
print(res)

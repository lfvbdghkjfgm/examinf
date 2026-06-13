# Solved by lfvbdghkjfgm
# https://lfvb.ru

from math import prod

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

res = 0

for x in nums:
    t = [min(x), max(x)]
    k = 0
    if x.count(max(x)) == 1:
        k += 1
    if x[0] not in t and x[-1] not in t:
        k += 1
    if prod(sorted(x)[-3:]) % min(x) == 0:
        k += 1
    if k == 1:
        res += 1
print(res)

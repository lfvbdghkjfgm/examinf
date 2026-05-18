# Solved by lfvbdghkjfgm
# https://lfvb.ru

import ipaddress as ip
from itertools import product, permutations
from collections import Counter

nums = [[int(i) for i in j.split(";")] for j in open("414_1.csv")]
res = 0
for x in nums:
    d = dict(Counter(x))
    if sorted(list(d.values())) == [1, 1, 1, 3]:
        j = [i for i in x if x.count(i) > 1]
        j1 = [i for i in x if x.count(i) == 1]
        if sum(j) > (sum(j1) / len(j1)):
            res += 1

print(res)
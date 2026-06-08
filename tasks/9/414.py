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

# Solved by София

l = [[int(d) for d in x.split()] for x in open("1")]
ct = 0
for x in l:
    povt3 = [a for a in x if x.count(a) == 3]
    if len(povt3) == 3 and len(set(x)) == 4:
        nepovt = [a for a in x if x.count(a) == 1]
        if sum(nepovt) / len(nepovt) < sum(povt3):
            ct += 1
print(ct)

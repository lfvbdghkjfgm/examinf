# Solved by lfvbdghkjfgm
# https://lfvb.ru

from collections import Counter
res = 0

nums = [[int(i) for i in x.split()] for x in open('1')]

for x in nums:
    d=  dict(Counter(x))
    if sorted(d.values()) == [1,1,1,2,3]:
        p = [i for i in x if d[i] > 1]
        np = [i for i in x if d[i] == 1]
        if sum(p) > sum(np):
            res = sum(x)

print(res)
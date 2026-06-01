# Solved by lfvbdghkjfgm
# https://lfvb.ru

from collections import Counter

nums = [[int(i) for i in x.split()] for x in open("1")]

st1 = [x[0] for x in nums]
st6 = [x[-1] for x in nums]
res = 0

for x in nums:
    d = dict(Counter(x))
    if sorted(d.values()) == [1, 1, 1, 3]:
        p = list(set([i for i in x if d[i] == 3]))
        np = list(set([i for i in x if d[i] == 1]))
        if st1.count(p[0]) == 337 or any([st6.count(i) == 337 for i in np]):
            res += 1
print(res)

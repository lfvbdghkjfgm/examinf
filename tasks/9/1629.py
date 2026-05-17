# Solved by lfvbdghkjfgm
# https://lfvb.ru

from collections import Counter

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

res = 0

for idx, x in enumerate(nums, 1):
    d = dict(Counter(x))
    if sorted(d.values()) in [[1, 1, 1, 1, 1, 3], [1, 1, 1, 1, 4]] and d[max(x)] in [
        3,
        4,
    ]:
        np = sorted([i for i in x if d[i] == 1])
        if np[0] + np[-1] <= sum(np[1:-1]):
            res += 1

print(res)

# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

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

# Solved by Иса


k = 0
l = [[int(d) for d in x.split()] for x in open("38")]
for x in l:
    povt1 = [d for d in x if x.count(d) == 1]
    x = sorted(x)
    if (x[-1] == x[-2] == x[-3] == x[-4] and len(povt1) == 4) or (
        x[-1] == x[-2] == x[-3] and len(povt1) == 5
    ):
        if max(povt1) + min(povt1) <= sum(povt1) - max(povt1) - min(povt1):
            k += 1
print(k)

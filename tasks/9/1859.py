# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from collections import Counter

nums = [[int(i) for i in x.split()] for x in open("1.txt")]

for x in nums:
    d = dict(Counter(x))
    if sorted(d.values()) == [1, 3, 3] and [a for a, b in d.items() if b == 1][
        0
    ] <= min([a for a, b in d.items() if b != 1]):
        print(max([a for a, b in d.items() if b != 1]))
        break

# Solved by София


l = [[int(d) for d in x.split()] for x in open("1859_1.csv")]
k = 0
for x in l:
    k += 1
    povt3 = [a for a in x if x.count(a) == 3]
    povt1 = [a for a in x if x.count(a) == 1]
    povt = [a for a in x if x.count(a) > 1]
    if len(povt3) == 6 and len(povt1) == 1:
        if povt1[0] <= min(povt):
            print(k, x)

# Solved by Аня


l = [[int(d) for d in x.split()] for x in open("1859.txt")]
k = 0
for x in l:
    k += 1
    p3 = [y for y in x if x.count(y) == 3]
    p1 = [y for y in x if x.count(y) == 1]
    if len(p3) == 6 and len(p1) == 1:
        if str(p1)[0] <= str(p3)[0]:
            print(k, x)

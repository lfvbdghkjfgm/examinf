# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return res


k = 0
for i in range(1_125_001, 10**10):
    t = dels(i)
    t = [j for j in t if j % 10 == 7 and j not in [7, i]]
    if t:
        print(i, min(t))
        k += 1
    if k == 5:
        break

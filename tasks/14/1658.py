# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def to_75(num):
    res = []
    while num:
        res.append(num % 75)
        num //= 75
    return res[::-1]


mn = 10**10

for x in range(1, 32001):
    t = to_75(75**314 + 75**118 - x)
    if t.count(0) < mn:
        mn = t.count(0)

print(mn)

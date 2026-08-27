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
for i in range(700_001, 10**10):
    t = dels(i)
    if t:
        m = max(t) + min(t)
        if m % 10 == 4:
            print(i, m)
            k += 1
    if k == 5:
        break

# Solved by Вадим С.


def dels(x):
    k = []
    for d in range(2, int(x**0.5) + 1):
        if x % d == 0:
            k.append(x // d)
            k.append(d)
    return max(k) + min(k) if len(k) > 0 else 0


for x in range(700_000, 705_000):
    m = dels(x)
    if m % 10 == 4:
        print(x, m)

# Solved by Аня


def dels(d):
    l = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            l.append(x)
            l.append(d // x)
    return sorted(set(l))


for x in range(700_001, 1_000_000):
    s = dels(x)
    if len(s) > 0:
        m = s[0] + s[-1]
        if str(m)[-1] == "4":
            print(x, m)

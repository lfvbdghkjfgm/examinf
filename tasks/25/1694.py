# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def prime_dels(num):
    res = []
    i = 2
    while i <= int(num**0.5):
        while num % i == 0:
            res.append(i)
            num //= i
        i += 1
    if num > 1:
        res.append(num)
    return res


k = 0
for i in range(5_700_001, 10**10):
    t = prime_dels(i)
    if len(t) > 1:
        m = max(t) + min(t)
        if m > 70_000 and int(m**0.5) ** 2 == m:
            print(i, m)
            k += 1
    if k == 5:
        break

# Solved by Иван П.


def pros(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return n > 1


def m(n):
    dels = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if pros(i):
                dels.append(i)
            if pros(n // i):
                dels.append(n // i)
    if len(dels) == 0:
        return 0
    dels = sorted(set(dels))
    return dels[0] + dels[-1]


for n in range(5700000, 5800000):
    mm = m(n)
    if mm > 70000:
        if int(mm**0.5) ** 2 == mm:
            print(n, mm)

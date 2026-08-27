# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def prime_dels(num):
    res = []
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            res.append(i)
        while num % i == 0:
            num //= i
        i += 1
    if num > 1:
        res.append(num)
    return res


k = 0
for i in range(4_444_000 - 1, 0, -1):
    s = sum(prime_dels(i))
    if s > 2_000_000 and s % 123 == 0:
        print(i, s)
        k += 1
    if k == 5:
        break

# Solved by Владимир Д.


def dels(d):
    dls = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            dls.append(x)
            dls.append(d // x)

    return sorted(set(dls))


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1


ct = 0
for n in range(4_444_000 - 1, -1, -1):
    dls = [d for d in dels(n) if d != n and is_prime(d)]

    if dls:
        s = sum(dls)
    else:
        continue

    if s > 2_000_000 and s % 123 == 0:
        ct += 1
        print(n, s)

    if ct == 5:
        break

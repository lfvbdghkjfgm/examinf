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


def is_prime(num):
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


k = 0
for i in range(5_000_001, 10**10):
    t = prime_dels(i)
    if (
        len(t) == 2
        and len(set(t)) == 2
        and all([j % 2 != 0 for j in t])
        and is_prime(abs(t[0] - t[1]))
    ):
        print(i, max(t))
        k += 1
    if k == 5:
        break

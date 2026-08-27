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
for i in range(2_400_001, 10**10):
    t = prime_dels(i)
    if (
        all(["4" in str(j) or "7" in str(j) for j in t])
        and len(t) == 3
        and len(set(t)) == 3
    ):
        print(i, max(t))
        k += 1
    if k == 5:
        break

# Solved by Анастасия


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1


def dels(d):
    s = []
    for x in range(1, int(d**0.5) + 1):
        if (
            d % x == 0
            and is_prime(x)
            and (str(x).count("4") >= 1 or str(x).count("7") >= 1)
        ):
            s.append(x)
        if (
            d % x == 0
            and is_prime(d // x)
            and (str(d // x).count("4") >= 1 or str(d // x).count("7") >= 1)
        ):
            s.append(d // x)
    return sorted(set(s))


for x in range(2400000, 10**10):
    d = dels(x)
    if len(d) == 3 and ((d[0] * d[1] * d[2]) == x):
        print(x, max(d))

# Solved by Аня


def is_prime(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return n > 1


def dels(d):
    s = []
    for x in range(1, int(d**0.5) + 1):
        if d % x == 0:
            if is_prime(x) and (str(x).count("4") >= 1 or str(x).count("7") >= 1):
                s.append(x)
            if is_prime(d // x) and (
                str(d // x).count("4") >= 1 or str(d // x).count("7") >= 1
            ):
                s.append(d // x)
    return sorted(set(s))


for x in range(2_400_001, 5_000_000):
    m = dels(x)
    if len(m) == 3 and x == m[0] * m[1] * m[2]:
        print(x, max(m))

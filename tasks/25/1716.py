# Solved by lfvbdghkjfgm
# https://lfvb.ru


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
for i in range(4_000_001, 10**10):
    t = prime_dels(i)
    if len(t) == 3 and all(["3" in str(j) and "5" in str(j) for j in t]):
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
        if d % x == 0 and is_prime(x) and ("3" in str(x) and "5" in str(x)):
            s.append(x)
        if (
            d % x == 0
            and is_prime(d // x)
            and ("3" in str(d // x) and "5" in str(d // x))
        ):
            s.append(d // x)
    return sorted(set(s))


for x in range(4_000_001, 10**8):
    d = dels(x)
    if len(d) == 2 and (d[0] * d[1] * d[1] == x or d[0] * d[0] * d[1] == x):
        print(x, max(d))

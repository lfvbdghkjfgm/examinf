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
for i in range(5_700_001, 10**10):
    t = prime_dels(i)
    if len(t) > 1:
        m = max(t) + min(t)
        if m > 70_000 and int(m**0.5) ** 2 == m:
            print(i, m)
            k += 1
    if k == 5:
        break
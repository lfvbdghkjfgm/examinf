# Solved by lfvbdghkfjgm
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
    return set(res)


k = 0
for i in range(7_800_000, 10**10):
    t = prime_dels(i)
    t1 = [j for j in t if j != i]
    if len(t1) >= 2:
        m = min(t1) + max(t1)
        if m % 100 == 63 and m % len(t) == 0:
            print(i, m)
            k += 1
    if k == 5:
        break

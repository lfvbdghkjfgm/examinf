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
for i in range(750_000, 1, -1):
    t = prime_dels(i)
    t = [j for j in t if j % 10 == 7 and j != i]
    if t:
        f = sum(t) // len(t)
        if f % 111 == 0:
            print(i, f)
            k += 1
    if k == 5:
        break
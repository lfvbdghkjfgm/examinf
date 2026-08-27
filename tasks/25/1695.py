# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


k = 0
for i in range(1_350_051, 10**10):
    d = dels(i)
    t = [j for j in d if j % 100 == 11 and j not in [i, 11]]
    if t:
        print(i, min(t))
        k += 1
    if k == 5:
        break

# Solved by Иван П.


def d11(n):
    d = 0
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if i % 100 == 11 and i != 11:
                d = i
                break
            if n // i % 100 == 11 and n // i != 11:
                d = n // i
                break
    return d


for n in range(1350051, 1500000):
    d = d11(n)
    if d != 0:
        print(n, d)

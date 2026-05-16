# Solved by lfvbdghkjfgm
# https://lfvb.ru


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return res


k = 0
for i in range(500_001, 10**10):
    t = dels(i)
    r = sum(t)
    if r % 10 == 9:
        print(i, r)
        k += 1
    if k == 5:
        break
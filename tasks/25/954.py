# Solved by lfvbdghkjfgm
# https://lfvb.ru


def dels(num):
    res = set()
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            res.add(i)
            res.add(num // i)
    return sorted(list(res))


for i in range(112_500_000, 112_550_001):
    t = dels(i)
    if len(t) >= 2:
        if (t[-1] + t[-2]) % 10_000 == 1214:
            print(i)

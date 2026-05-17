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
for i in range(700_001, 10**10):
    t = dels(i)
    if t:
        m = max(t) + min(t)
        if m % 10 == 4:
            print(i, m)
            k += 1
    if k == 5:
        break

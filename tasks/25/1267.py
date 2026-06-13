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

# Solved by Аня


def dels(d):
    s = []
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            s.append(x)
            s.append(d // x)
    return sorted(set(s))


for x in range(500_001, 10**6):
    m = dels(x)
    if len(m) > 0:
        r = sum(m)
        if str(r)[-1] == "9":
            print(x, r)

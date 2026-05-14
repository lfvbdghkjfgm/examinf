# Solved by lfvbdghkjfgm
# https://lfvb.ru

def primitive_roots(num):
    res = []
    i = 2
    while i < int(num**0.5) + 1:
        if num % i == 0:
            res.append(i)
            while num % i == 0:
                num //= i
        i += 1
    if num > 1:
        res.append(num)
    return res


k = 0
for i in range(1_000_001, 10**10):
    t = primitive_roots(i)
    if len(t) == 3:
        print(i, max(t))
        k += 1
    if k == 5:
        break
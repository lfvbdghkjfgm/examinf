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

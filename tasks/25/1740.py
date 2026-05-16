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
for i in range(2_400_001, 10**10):
    t = prime_dels(i)
    if (
        all(["4" in str(j) or "7" in str(j) for j in t])
        and len(t) == 3
        and len(set(t)) == 3
    ):
        print(i, max(t))
        k += 1
    if k == 5:
        break
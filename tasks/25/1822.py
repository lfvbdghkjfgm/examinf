# Solved by lfvbdghkfjgm
# https://lfvb.ru


def prime_dels(num):
    res = []
    i = 2
    while i <= int(num**0.5):
        if num % i == 0:
            res.append(i)
        while num % i == 0:
            num //= i
        i += 1
    if num > 1:
        res.append(num)
    return res


k = 0
for i in range(4_444_000 - 1, 0, -1):
    s = sum(prime_dels(i))
    if s > 2_000_000 and s % 123 == 0:
        print(i, s)
        k += 1
    if k == 5:
        break

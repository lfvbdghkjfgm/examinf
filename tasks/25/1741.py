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


def check(l):
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            if l[i] + l[j] == 2026:
                return True
    return False


k = 0
for i in range(20262027, 10**10):
    t = prime_dels(i)
    if check(t):
        print(i, max(t))
        k += 1
    if k == 5:
        break
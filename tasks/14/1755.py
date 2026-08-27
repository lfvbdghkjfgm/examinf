# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def is_prime(num):
    if num in [0, 1]:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def to_243(num):
    res = []
    while num:
        res.append(num % 243)
        num //= 243

    return res[::-1]


t = to_243(20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30)
print(len([i for i in t if i < 20 and is_prime(i)]))

# Solved by Данзан С.


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False
    return d > 1


def v243(d):
    s = []
    while d > 0:
        s.append(d % 243)
        d //= 243
    return s[::-1]


d = 20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30
d = v243(d)
ct = 0
for x in d:
    if x <= 20 and is_prime(x):
        ct += 1
        print(x)
print(ct)

# Solved by Владимир Д.


def to243(n):
    r = []
    while n > 0:
        r.append(n % 243)
        n //= 243
    return r[::-1]


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1


s = to243(20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30)
print(len(list(d for d in s if d < 20 and is_prime(d))))

# Solved by Глеб Г.


def f(n):
    l = []
    while n > 0:
        l.append(n % 243)
        n //= 243
    return l[::-1]


def ip(n):
    for x in range(2, int(n**0.5) + 1):
        if n % x == 0:
            return False
    return n > 1


a = 20 * 3**243 + 17 * 81**70 + 14 * 243**35 + 254 - 224 * 3**30
a = f(a)
ct = 0
for y in a:
    if ip(y) and y < 20:
        ct += 1
print(ct)

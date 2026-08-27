# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def to_11(num):
    res = []
    while num:
        res.append(num % 11)
        num //= 11
    return res[::-1]


for x in range(1, 3001):
    t = to_11(9 * 11**210 + 8 * 11**150 - x)
    if t.count(0) == 60:
        print(x)

# Solved by Анастасия


def v11(d):
    s = []
    while d > 0:
        s.append(d % 11)
        d //= 11
    return s[::-1]


for x in range(1, 3001):
    d = 9 * 11**210 + 8 * 11**150 - x
    d = v11(d)
    if d.count(0) == 60:
        print(x)

# Solved by Глеб Г.


def f(n):
    l = []
    while n > 0:
        l.append(n % 11)
        n //= 11
    return l[::-1]


for x in range(1, 3001):
    a = 9 * 11**210 + 8 * 11**150 - x
    a = f(a)
    if a.count(0) == 60:
        print(x)

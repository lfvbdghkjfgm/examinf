# Solved by Аня


def v13(n):
    s = []
    while n > 0:
        s.append(n % 13)
        n //= 13
    return s[::-1]


for x in range(1, 5000):
    d = 7 * 13**180 + 5 * 13**120 - x
    d = v13(d)
    if d.count(0) == 60:
        print(x)

# Solved by Владимир Д.


def to13(s):
    res = []
    while s > 0:
        res.append(s % 13)
        s //= 13

    return res[::-1]


for x in range(1, 5000):
    n = to13(7 * 13**180 + 5 * 13**120 - x)
    ct0 = [d for d in n if d == 0]
    if len(ct0) == 60:
        print(x)

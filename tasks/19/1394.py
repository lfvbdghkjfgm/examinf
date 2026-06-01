# Solved by Вадим С.


def f(s, p):
    if s >= 128 and p == 2:
        return 1
    if s >= 128 and p == 1:
        return 0
    if s < 128 and p == 2:
        return 0
    if p % 2 == 0:
        return f(s + 2, p + 1) and f(s + 5, p + 1) and f(s * 2, p + 1)
    else:
        return f(s + 2, p + 1) or f(s + 5, p + 1) or f(s * 2, p + 1)


for x in range(1, 128):
    if f(x, 0):
        print(x)
        break


def f(s, p):
    if s >= 128 and p == 3:
        return 1
    if s >= 128 and p == 2:
        return 0
    if s < 128 and p == 3:
        return 0
    if p % 2 != 0:
        return f(s + 2, p + 1) and f(s + 5, p + 1) and f(s * 2, p + 1)
    else:
        return f(s + 2, p + 1) or f(s + 5, p + 1) or f(s * 2, p + 1)


for x in range(1, 128):
    if f(x, 0):
        print(x)


def f(s, p):
    if s >= 128 and (p == 2):
        return 1
    if s >= 128 and (p == 1 or p == 3):
        return 0
    if s < 128 and p == 2:
        return 0
    if p % 2 == 0:
        return f(s + 2, p + 1) and f(s + 5, p + 1) and f(s * 2, p + 1)
    else:
        return f(s + 2, p + 1) or f(s + 5, p + 1) or f(s * 2, p + 1)


for x in range(1, 128):
    if f(x, 0):
        print(x)

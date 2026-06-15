# Solved by lfvbdghkjfgm
# https://lfvb.ru


def f(n, c):
    if n == c:
        return 1
    if n < c:
        return 0
    return f(n - 2, c) + f(n // 2, c)


print(f(38, 16) * f(16, 2))

# Solved by Глеб Г.


def f(x, y):
    if x < y:
        return 0
    if x == y:
        return 1
    if x > y:
        return f(x - 2, y) + f(x // 2, y)


print(f(38, 16) * f(16, 2))

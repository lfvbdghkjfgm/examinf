# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


def f(n, c):
    if n == c:
        return 1
    if n < c:
        return 0
    if n == 23:
        return 0
    return f(n - 1, c) + f(n - 5, c) + f(n // 3, c)


print(f(36, 21) * f(21, 15) * f(15, 5))

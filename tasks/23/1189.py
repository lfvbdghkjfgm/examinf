# Solved by lfvbdghkjfgm
# https://lfvb.ru


def f(n, c):
    if n == c:
        return 1
    if n < c:
        return 0
    if n == 28:
        return 0
    if n % 2 == 0:
        return f(n - 2, c) + f(n // 2, c)
    else:
        return f(n - 2, c) + f(n - 3, c)


print(f(98, 1))

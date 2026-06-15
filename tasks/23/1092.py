# Solved by lfvbdghkjfgm
# https://lfvb.ru


def f(n, c):
    if n == c:
        return 1
    if n > c:
        return 0
    return f(n + 1, c) + f(n + 2, c)


print(f(1, 11))

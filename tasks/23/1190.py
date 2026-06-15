# Solved by lfvbdghkjfgm
# https://lfvb.ru


def f(n, c):
    if n == c:
        return 1
    if n > c:
        return 0
    return f(n + 2, c) + f(n * 4, c)


print(f(3, 200) * f(200, 510))

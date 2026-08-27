# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from functools import lru_cache


@lru_cache(None)
def f(n):
    if n >= 21:
        return f(n - 8) + 1095
    return 10 * (g(n - 7) - 36)


@lru_cache(None)
def g(n):
    if n >= 22560:
        return n / 23 + 33
    return g(n + 11) - 4


for i in range(23_000, 0, -1):
    g(i)

for i in range(600):
    f(i)

print(f(548))

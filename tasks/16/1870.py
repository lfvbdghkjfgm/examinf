# Solved by lfvbdghkjfgm
# https://lfvb.ru

from functools import lru_cache


@lru_cache(None)
def f(n):
    return 3 * g(n - 3) + 7


@lru_cache(None)
def g(n):
    if n <= 20:
        return n + 2
    return g(n - 3) + 1


for i in range(40_000):
    g(i)

print(f(37811))

# Solved by Анастасия


import sys

sys.setrecursionlimit(1000000)


def g(n):
    if n <= 20:
        return n + 2
    if n > 20:
        return g(n - 3) + 1


def f(n):
    return 3 * g(n - 3) + 7


print(f(37811))

# Solved by Аня


import sys

sys.setrecursionlimit(10**6)


def f(n):
    return 3 * g(n - 3) + 7


def g(n):
    if n <= 20:
        return n + 2
    else:
        return g(n - 3) + 1


print(f(37811))

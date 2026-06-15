# Solved by Влад


from functools import *


@lru_cache(None)
def g(n):
    if n >= 248045:
        return (n / 20) + 28
    if n < 248045:
        return g(n + 9) - 4


@lru_cache(None)
def f(n):
    if n >= 19:
        return f(n - 4) + 3580
    if n < 19:
        return 6 * (g(n - 7) - 36)


for n in range(248045, 673, -1):
    g(n)
for n in range(19, 673):
    f(n)
print(f(673))

# Solved by Анастасия


import sys

sys.setrecursionlimit(1000000)


def g(n):
    if n >= 248045:
        return (n / 20) + 28
    if n < 248045:
        return g(n + 9) - 4


sys.setrecursionlimit(1000000)


def f(n):
    if n >= 19:
        return (f(n - 4)) + 3580
    if n < 19:
        return 6 * (g(n - 7) - 36)


print(f(673))

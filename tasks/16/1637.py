# Solved by Влад


from sys import *

setrecursionlimit(10**9)
from functools import *


@lru_cache(None)
def g(n):
    if n < 9999:
        return 15 * (2 * n + 4)
    if n >= 9999:
        return g(n - 5) + g(n - 3) + 157


@lru_cache(None)
def f(n):
    if n >= 57000:
        return f(n - 2) + 3552 + f(n - 3)
    if n < 57000:
        return 222 + g(n - 2) + g(n - 1)


for n in range(2540, 9999):
    g(n)
for n in range(2540, 57000):
    f(n)
print(f(2540))
print(1 * 5 * 2 * 6 * 5 * 2)

# Solved by Мария


import functools


@functools.lru_cache(3000)
def F(n):
    if n >= 57000:
        return F(n - 2) + 3552 + F(n - 3)
    if n < 57000:
        return 222 + G(n - 2) + G(n - 1)


@functools.lru_cache(50000)
def G(n):
    if n >= 9999:
        return G(n - 5) + G(n - 3) + 157
    if n < 9999:
        return 15 * (2 * n + 4)


print(F(2540))

# Solved by Анастасия

import sys

sys.setrecursionlimit(1000000)


def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + f(n - 1)


print((sum(map(int, str(f(57693))))) ** 2)

# Solved by Аня

import sys, functools

sys.setrecursionlimit(10**6)


@functools.lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return 2 * n + f(n - 1)


for x in range(1, 100_000):
    f(x)
z = f(57693)
print(z)
print(((sum(map(int, str(z))))) ** 2)

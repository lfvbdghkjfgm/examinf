# Solved by Аня


import sys, functools

sys.setrecursionlimit(10**6)


@functools.lru_cache((None))
def f(n):
    return 3 * (g(n - 4) + 5)


@functools.lru_cache((None))
def g(n):
    if n < 8:
        return 3 * n
    else:
        return g(n - 3) + 2


for x in range(1, 20_000):
    f(x)
for x in range(100, 1, -1):
    g(x)
print(f(12345))

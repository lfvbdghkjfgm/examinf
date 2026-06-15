# Solved by Влад


from functools import *


@lru_cache(None)
def g(n):
    if n >= 301208:
        return 10 * n + 50
    if n < 301208:
        return g(n + 7) - 21


@lru_cache(None)
def f(n):
    if n > 40:
        return f(n - 4) + 3020
    if n <= 40:
        return 3 * (g(n - 2) - 15)


for n in range(301208, 5077, -1):
    g(n)
for n in range(40, 5079):
    f(n)
print(f(5078))

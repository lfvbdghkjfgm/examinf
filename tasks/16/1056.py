# Solved by Влад


from functools import *


@lru_cache(100)
def f(n):
    if n >= 6:
        return 3 * n * f(n - 3)
    if n < 6:
        return n


for n in range(6, 12572):
    if n == 12565:
        x3 = f(12565)
    elif n == 12568:
        x2 = f(12568)
    elif n == 12571:
        x1 = f(12571)
    else:
        f(n)
print((x1 - 9 * x2) / x3)

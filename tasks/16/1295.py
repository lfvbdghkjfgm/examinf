# Solved by Влад

from functools import *


@lru_cache(None)
def f(n):
    if n <= 5:
        return 1
    if n > 5:
        return n + f(n - 2)


for n in range(1, 2126):
    f(n)
print(f(2126) - f(2122))

# Solved by lfvbdghkjfgm
# https://lfvb.ru

from functools import lru_cache


@lru_cache(1000)
def f(n):
    if n < 10:
        return 1
    return (n + 3) * f(n - 3)


for i in range(247563):
    f(i)

print((f(247563) - f(247560) * 519 * 477) / (f(247557) * 519))

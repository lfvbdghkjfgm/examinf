# Solved by lfvbdghkjfgm
# https://lfvb.ru

from functools import lru_cache


@lru_cache(100)
def f(n):
    if n < 17:
        return 6
    return (n + 5) * f(n - 9)


for i in range(234561):
    f(i)

print((f(234561) * 218 + f(234552) * 436) / (218 * 436 * f(234534)))

# Solved by Данзан С.


import sys, functools

sys.setrecursionlimit(1000000)


@functools.lru_cache(None)
def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * F(1 - n) + 3 * F(n - 1) + 2
    if n < 0:
        return -F(-n)


for x in range(15000):
    F(x)
print(F(14750))

# Solved by Мария


import sys, functools

sys.setrecursionlimit(10000000)


@functools.lru_cache(15000)
def F(n):
    if n == 0:
        return 1
    if n > 0:
        return 2 * F(1 - n) + 3 * F(n - 1) + 2
    if n < 0:
        return -F(-n)


for x in range(14750):
    F(x)
x = F(14750)
print(sum(map(int, str(x))))

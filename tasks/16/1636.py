# Solved by lfvbdghkjfgm
# https://lfvb.ru

from functools import lru_cache

@lru_cache(None)
def f(n):
    if n < 65_000:
        return f(9+n) + 13020
    return  4* (g(n-4)-12)

@lru_cache(None)
def g(n):
    if n>=111700:
        return g(n-17)+344
    return 8*n-4

for i in range(100_000,10**6):
    g(i)

for i in range(70_000,2000,-1):
    f(i)

print(f(4975))
print(2*sum(map(int,str(f(4975)))))
print(8+8+9+2+3+3+6+8)
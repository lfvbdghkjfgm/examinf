# Solved by Влад


from sys import *

set_int_max_str_digits(50000)
from functools import *


@lru_cache(None)
def f(n):
    if n == 1:
        return 1
    if n > 1:
        return f(n - 1) * (n // 2) + 1


for n in range(1, 10000):
    f(n)
print(str(f(10000))[-18:])
s = "995857660475895001"
d = sum([int(x) for x in s])
print(d)

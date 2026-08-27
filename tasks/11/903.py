# Solved by Виктор Г.


import math

for x in range(1000):
    f = math.log((10 + 52 + x), 2)
    k = (53 * f) / 8
    t = 93 * 1024
    if k * 2000 <= t and f.is_integer():
        print(x)

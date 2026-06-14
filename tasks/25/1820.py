# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re
from math import isqrt

squares = [7**i for i in range(1, 8)]
k = 0
for i in range(8_700_000 - 1, 0, -1):
    if "1" in str(i) or "3" in str(i):
        for j in squares:
            if (i - j) % 4 == 0:
                if isqrt(i - j) ** 2 == i - j:
                    print(i, squares.index(j) + 1)
                    k += 1
                    break
    if k == 5:
        break

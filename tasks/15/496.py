# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

from itertools import product

for A in range(1000, 0, -1):
    if all(
        [
            (x + y <= 24) or (y <= x - 2) or (y >= A)
            for x, y in product(range(1, 200), repeat=2)
        ]
    ):
        print(A)
        break

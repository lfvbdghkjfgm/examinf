# Solved by lfvbdghkjfgm
# https://lfvb.ru

from itertools import product

for A in range(1000):
    if all(
        [
            (x**2 + y**2 > 1024 - x) or (y < -2 * x + A)
            for x, y in product(range(1000), repeat=2)
        ]
    ):
        print(A)
        break

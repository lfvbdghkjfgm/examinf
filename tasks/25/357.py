# Solved by Владимир Д.

import fnmatch

mask = "7*53?3*1"


def is_prime(d):
    for x in range(2, int(d**0.5) + 1):
        if d % x == 0:
            return False

    return d > 1


for i in range(2627, 10**9, 2627):
    sm = sum(list(map(int, str(i))))
    if is_prime(sm):
        if fnmatch.fnmatch(str(i), mask):
            print(i, i // 2627)

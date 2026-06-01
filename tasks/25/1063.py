# Solved by Данзан С.

import fnmatch

for x in range(27451, 10**10, 27451):
    if fnmatch.fnmatch(str(x), "54?1?3*7"):
        if x % 27451 == 0:
            print(x, x // 27451)

# Solved by Глеб Г.

import fnmatch

for x in range(27451, 10**10, 27451):
    if fnmatch.fnmatch(str(x), "54?1?3*7"):
        print(x, x // 27451)

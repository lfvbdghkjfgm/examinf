# Solved by Аня

import fnmatch

for x in range(2024, 10**10, 2024):
    if sum(map(int, str(x))) % 2 != 0:
        if fnmatch.fnmatch(str(x), "112?57*4"):
            print(x, x // 2024)

# Solved by Владимир Д.

import fnmatch

mask = "112?57*4"
for s in range(2024, 10**10, 2024):
    sm = sum(list(map(int, str(s))))
    if s % 2024 == 0:
        if sm % 2 != 0:
            if fnmatch.fnmatch(str(s), mask):
                print(s, s // 2024)

# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

for i in range(2026, 10**10, 2026):
    if re.fullmatch(r"21\d*93\d3\d*5\d2", str(i)):
        print(i, i // 2026)

# Solved by Аня


import fnmatch

for x in range(2026, 10**10, 2026):
    if fnmatch.fnmatch(str(x), "21*93?3*5?2"):
        print(x, x // 2026)

# Solved by Владимир Д.


import fnmatch

mask = "21*93?3*5?2"

for s in range(2026, 10**10, 2026):
    if fnmatch.fnmatch(str(s), mask):
        print(s, s // 2026)

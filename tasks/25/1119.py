# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re
from collections import Counter

for i in range(123456789, 10**14, 123456789):
    if re.fullmatch(r"7\d3\d5\d*9", str(i)):
        d = dict(Counter(list(str(i))))
        if 5 in d.values():
            print(i, i // 123456789)

# Solved by Владимир Д.


import fnmatch

mask = "7?3?5*9"

for s in range(123456789, 10**14, 123456789):
    ls = list(map(int, str(s)))
    usl1 = [d for d in ls if ls.count(d) == 5]
    if len(usl1) == 5:
        if fnmatch.fnmatch(str(s), mask):
            print(s, s // 123456789)

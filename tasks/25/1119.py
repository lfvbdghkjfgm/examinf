# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re
from collections import Counter

for i in range(123456789, 10**14, 123456789):
    if re.fullmatch(r"7\d3\d5\d*9", str(i)):
        d = dict(Counter(list(str(i))))
        if 5 in d.values():
            print(i, i // 123456789)
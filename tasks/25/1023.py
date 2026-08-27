# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

for i in range(18579, 10**10, 18579):
    if re.fullmatch(r"54\d1\d3\d*7", str(i)):
        print(i, i // 18579)

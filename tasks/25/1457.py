# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

for i in range(154682, 10**11, 154682):
    if re.fullmatch(r"\d*192\d3\d*68", str(i)):
        print(i, i // 154682)

# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

k = 0
for i in range(10980, 10**10, 10980):
    if re.fullmatch(r"20[13579]{2}22[02468]*", str(i)):
        print(i, i // 10980)
        k += 1
    if k == 5:
        break

# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

k = 1
for i in range(206, 10**8 + 1, 206):
    if re.fullmatch(r"123\d*[13579][02468]56", str(i)):
        print(i, i // 206)

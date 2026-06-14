# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1553_1.txt").read()

m = re.findall(r"[^CF]+", text)

print(len(max(m, key=len)))

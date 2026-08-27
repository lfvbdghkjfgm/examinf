# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1566_1.txt").read()

m = re.findall(r"(?:\d{2}[ABC])+", text)

print(len(max(m, key=len)) / 3)

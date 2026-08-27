# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1458_1.txt").read()
num = r"(?:[1-9][0-9]*|0)"
m = re.findall(rf"\(((?:{num}\+)+{num})\)", text)
m = [i for i in m if eval(i) % 2 == 0]
print(len(max(m, key=len)) + 2)

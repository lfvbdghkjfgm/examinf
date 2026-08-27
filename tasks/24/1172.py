# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1172_1.txt").read()

num = r"[1-9][0-9]*"
m = re.findall(rf"(?:{num}[+*])+{num}", text)

mx = 0
for i in m:
    i = i.replace("*", "+")
    i = i.split("+")
    mx = max(mx, len(i))
print(mx)

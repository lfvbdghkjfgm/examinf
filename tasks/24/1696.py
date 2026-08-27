# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1696_1.txt").read()

A = r"(?:[1-9][0-9]*[12346789]|[12346789])"
B = r"(?:[1-9][0-9]*[05]|[05])"
group = rf"\((?:{A}[-+]{B})\)"

m = re.findall(rf"(?:{group})+", text)
print(len(max(m, key=len)))

# Solved by Аня


import re

s = open("1696_1.txt").readline()
m = re.findall(r"(?:\([1-9]\d*[12346789][+-][1-9]\d*[05]\))+", s)
print(len(max(m, key=len)))

# Solved by Глеб Г.

import re

s = open("20.txt").readline()
m = re.findall(r"(?:(?:[1-9]\d*|0)[-*])+(?:[1-9]\d*|0)", s)
print(max(m, key=len))
print(len(max(m, key=len)))

# Solved by Аня

import re

s = open("1265_1.txt").readline()
m = re.findall(r"(?:(?:[7-9]\d*|0)[-*])+(?:[7-9]\d*|0)", s)
print(len(max(m, key=len)))

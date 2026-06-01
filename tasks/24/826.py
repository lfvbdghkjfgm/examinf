# Solved by Владимир Д.

import re

s = open("/home/student/Загрузки/826_1.txt").readline()

m = re.findall(r"A+(?:[1-9]+[-*])+\d+", s)
print(len(max(m, key=len)))

# Solved by Влад

from re import *

s = open("826_1.txt").readline()
s = s.replace("*", "-")
n = r"[1-6]+"
m = rf"A+{n}(-{n})*"
print(max([len(x.group()) for x in finditer(m, s)]))

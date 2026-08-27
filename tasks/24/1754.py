# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1754_1.txt").read()

m = re.findall(r"(?:[^.M]*M){112}[^.M]*\.", text)
print(len(max(m, key=len)))

# Solved by Анастасия


import re

m = open("1754.txt").readline()
s = re.findall(r"(?:[^M.]*M){112}[^M.]*\.", m)
print(len(max(s, key=len)))
print((max(s, key=len)))

# Solved by Иван С.


from re import *

s = open("1754_1.txt").readline()
m = findall(r"(?:[^M.]*M){112}[^M.]*\.", s)
print(len(max(m, key=len)))

# Solved by София


import re

t = open("1").readline()
m = re.findall(r"(?:[A-Z]+ )+[A-Z]+\.", t)
if m.count("M") == 112:
    print(len(max(m, key=len)))
    print((max(m, key=len)))


s = open("1").readline()
m = 0
c = ""
for r in range(len(s)):
    c += s[r]
    while c.count("M") > 112 or c.count(".") > 1:
        c = c[1:]
    if c.count("M") == 112 and c.count(".") == 1 and c[-1] == ".":
        m = max(len(c), m)
print(m)

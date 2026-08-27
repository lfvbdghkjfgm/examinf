# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\390_1.txt").read()

m = re.findall(r"[^AIEOUY]?(?:[AEOUYI][^AEOIUY])+[AEIOUY]?", text)
print(len(max(m, key=len)))

# Solved by Влад


from re import *

f = open("test.txt")
s = f.readline()
for c in "QWRTPSDFGHJKLZXCVBNM":
    s = s.replace(c, "!")
for c in "EYUIOA":
    s = s.replace(c, "@")
p = r"((!@)+!?|(@!)+@?)"
p2 = rf"(?=({p}))"
res = []
for x in finditer(p2, s):
    res.append(len(x.group(1)))
print(max(res))

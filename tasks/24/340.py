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

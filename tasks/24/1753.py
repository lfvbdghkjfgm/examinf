# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1753_1.txt").read()

m = re.findall(r"(?:[A-Z]+ +)*[A-Z]+\.", text)
res = []

for st in m:
    s = st[:-1].split()
    s = [len(i) for i in s]
    if s == sorted(s, reverse=True):
        res.append(st)
    else:
        for start in range(len(st)):
            if start == 0 or st[start] != " " and st[start - 1] == " ":
                s = st[start:-1].split()
                s = [len(i) for i in s]
                if s == sorted(s, reverse=True):
                    res.append(st[start:])
print(len(max(res, key=len)))

# Solved by Иван С.


from re import *

s = open("1753_1.txt").readline()
m = findall(r"[A-Z][^.]*[^ ]\.", s)
mx = 0
for x in m:
    c = ""
    for i in range(len(x) - 2, -1, -1):
        c = x[i] + c
        if c[0] == " ":
            continue
        lens = [len(j) for j in c.split()]
        if sorted(lens, reverse=True) == lens:
            mx = max(mx, len(c) + 1)

print(mx)

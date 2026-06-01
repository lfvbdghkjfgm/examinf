# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

with open("/home/student/Загрузки/511_1.txt") as f:
    text = f.read()

m = re.findall(r"\d+(?:[+*]\d+)+", text)


mx = 0
pr = ""
for i in m:
    s = i.split("+")
    s1 = []
    for g in s:
        s11 = g.split("*")
        f = 1
        for j in s11:
            f *= int(j)
        s1.append(f)
    if not sum(s1):
        if len(i) > mx:
            mx = len(i)
            pr = i
print(pr)

# Solved by lfvbdghkjfgm
# https://lfvb.ru

# СЂРµС€РµРЅРёРµ 1
import re

text = open(r"C:\Users\aatop\Downloads\1721_1.txt").read()

for i in "13579":
    text = text.replace(i, "*")

m = re.findall(r"G(?:[^G*]*\*){45}[^G*]*", text)
print(len(max(m, key=len)))

# СЂРµС€РµРЅРёРµ 2

import re

text = open(r"C:\Users\aatop\Downloads\1721_1.txt").read()

for i in "13579":
    text = text.replace(i, "*")

res = []
text = text.split("G")
for i in text[1:]:
    i = i.split("*")
    i = i[:46]
    i = "*".join(i)
    res.append("G" + i)
print(len(max(res, key=len)))

# Solved by Вадим С.

import re

l = open("1721_1.txt").readline()
l = l.replace("1", "#")
l = l.replace("3", "#")
l = l.replace("5", "#")
l = l.replace("7", "#")
l = l.replace("9", "#")
m = re.findall(r"G(?:[^G^#]*#){45}[^G^#]*", l)
print(max(m, key=len))
print(len(max(m, key=len)))

# Solved by Анастасия

import re

m = open("1721.txt").readline()
s = re.findall(r"G(?:[^13579G]*[13579]){45}[^13579G]*", m)
print(max(s, key=len))
print(len(max(s, key=len)))

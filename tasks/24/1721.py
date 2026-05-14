# Solved by lfvbdghkjfgm
# https://lfvb.ru

# решение 1
import re

text = open(r"C:\Users\aatop\Downloads\1721_1.txt").read()

for i in "13579":
    text = text.replace(i, "*")

m = re.findall(r"G(?:[^G*]*\*){45}[^G*]*", text)
print(len(max(m, key=len)))

# решение 2

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
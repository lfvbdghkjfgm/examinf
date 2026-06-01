# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1696_1.txt").read()
A = r"(?:[1-9][0-9]*[02468]|[02468])"
B = r"(?:[1-9][0-9]*[13579]|[13579])"
group = rf"\((?:{A}[-+]{B})\)"

m = re.findall(rf"(?:{group})+", text)
print(len(max(m, key=len)))

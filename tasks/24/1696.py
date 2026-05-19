# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1696_1.txt").read()

A = r"(?:[1-9][0-9]*[12346789]|[12346789])"
B = r"(?:[1-9][0-9]*[05]|[05])"
group = rf"\((?:{A}[-+]{B})\)"

m = re.findall(rf"(?:{group})+", text)
print(len(max(m, key=len)))
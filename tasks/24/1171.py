# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1171_1.txt").read()
number = r"(?:[1-9][0-9]*|0)"
m = re.findall(rf"(?:{number}[-*])+{number}", text)
print(len(max(m, key=len)))
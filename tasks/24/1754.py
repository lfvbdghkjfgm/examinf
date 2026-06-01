# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1754_1.txt").read()

m = re.findall(r"(?:[^.M]*M){112}[^.M]*\.", text)
print(len(max(m, key=len)))

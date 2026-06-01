# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1554_1.txt").read()

m = re.findall(r"\d+", text)

print(len(max(m, key=len)))

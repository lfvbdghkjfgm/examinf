# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1565_1.txt").read()

m = re.findall(r"(?=((?:BAC|CAB)+))", text)

print(len(max(m, key=len)))

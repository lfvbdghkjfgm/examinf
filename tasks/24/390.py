# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\390_1.txt").read()

m = re.findall(r"[^AIEOUY]?(?:[AEOUYI][^AEOIUY])+[AEIOUY]?", text)
print(len(max(m, key=len)))
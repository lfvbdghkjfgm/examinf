# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1731_1.txt").read()
text = text.replace("02", "*")
m = re.findall(r"(?:[^AEIOUY*]*\*){20}[^AEIOUY*]*[AEIOUY]", text)
print(len(max(m, key=len).replace("*", "02")) + 1)

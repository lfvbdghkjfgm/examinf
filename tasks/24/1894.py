# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\111\Downloads\24.txt").readline()

text = text.replace("20", "#")

m = re.findall(r"(?:#[^#AEIOUY]*){26}[^AEIOUY#]*[AEIOUY]", text)

print(len(min(m, key=len)) + 26)

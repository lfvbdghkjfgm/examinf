# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

with open("/home/student/Загрузки/1087_1.txt") as f:
    text = f.read()

m = re.findall(r"(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?", text)

print(len(max(m, key=len)))

# Solved by Аня


import re

m = open("1087_1.txt").readline()
s = re.findall(r"(?:LMN|MN|N)?(?:KLMN)+(?:KLM|KL|K)?", m)
print(s)
print(len(max(s, key=len)))
print((max(s, key=len)))

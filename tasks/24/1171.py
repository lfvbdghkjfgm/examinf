# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1171_1.txt").read()
number = r"(?:[1-9][0-9]*|0)"
m = re.findall(rf"(?:{number}[-*])+{number}", text)
print(len(max(m, key=len)))

# Solved by Владимир Д.

import re

text = open("other/examinf/24/1171.txt").read()
number = r"(?:[1-9][0-9]*|0)"
m = re.findall(rf"(?:{number}[-*])+{number}", text)
print(len(max(m, key=len)))

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

# Solved by Анастасия


import re

s = open("1171.txt").readline()
m = re.findall(r"(?:(?:[1-9]\d*|0)[-*])+(?:[1-9]\d*|0)", s)
print(len(max(m, key=len)))

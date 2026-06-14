# Solved by lfvbdghkjfgm
# https://lfvb.ru

import re

text = open(r"C:\Users\aatop\Downloads\1739_1.txt").read()
A = r"(?:[1-9][0-9]*[12346789]|[12346789])"
B = r"(?:[1-9][0-9]*[05]|[05])"
group = rf"\((?:{A}[-+]{B})\)"

m = re.findall(rf"(?:{group})+", text)
print(len(max(m, key=len)))

# Solved by Анастасия

import re

m = open("1739.txt").readline()
s = re.findall(r"(?:\([1-9][0-9]*[^50][+-][1-9][0-9]*[05]\))+", m)
print(len(max(s, key=len)))

# Solved by Иван С.

from re import *

s = open("1739_1.txt").readline()
m = findall(r"(?:\([1-9][0-9]*[12346789][+-][1-9][0-9]*[50]\))+", s)
print(len(max(m, key=len)))

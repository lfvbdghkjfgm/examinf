# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1698_1.txt").read()

m = re.findall(r"(?=([A-Za-z0-9.]+[A-Za-z0-9]@(?:yandex\.ru|gmail\.com)))", text)


print(len(max(m, key=len)))

# Solved by Влад


from re import *

f = open("test.txt")
s = f.readline()

v = r"(([0-9a-zA-Z.])+@(yandex.ru|gmail.com))"
p = rf"(?=({v}))"
for x in finditer(p, s):
    if ".." not in x.group(1) and ".@" not in x.group(1):
        print(x.group(1))
print(
    max(
        [
            len(x.group(1))
            for x in finditer(p, s)
            if ".." not in x.group(1) and ".@" not in x.group(1)
        ]
    )
)

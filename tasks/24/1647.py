# Solved by lfvbdghkfjgm
# https://lfvb.ru

import re


def spl(lst, sep):
    res = []
    for i in lst:
        res += i.split(sep)
    return res


text = open(r"C:\Users\aatop\Downloads\1647_1.txt").read()

text = spl(spl([text], "**"), "++")
text = spl(spl(text, "*0"), "+0")
res = 0
for st in text:
    mx = 0
    if len(st) < res:
        continue
    for start in range(len(st)):
        for end in range(start + 1, len(st) + 1):
            if end - start < mx:
                continue
            s = st[start:end]
            if (
                re.fullmatch(r"(?:(?:[1-9][0-9]*[+*])+[1-9][0-9]*|[1-9][0-9]*)", s)
                and eval(s) % 2 == 0
            ):
                mx = max(mx, len(s))
    res = max(res, mx)

print(res)

# Solved by Аня

import re

d = []
s = open("1647_1.txt").readline()
m = re.findall(r"(?:[1-9]\d*[+*])+[1-9]\d*", s)
print(max(m, key=len))
print(len(max(m, key=len)) - 2)

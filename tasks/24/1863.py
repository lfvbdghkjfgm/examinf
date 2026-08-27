# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf


text = open(r"C:\Users\111\Downloads\1863_1.txt").readline()


def smart_split(data: list, separator: str):
    res = []
    for st in data:
        res += st.split(separator)
    return res


mx = 0

text = smart_split([text], "++")
text = smart_split(text, "**")
text = smart_split(text, "*")

for st in text:
    st = st.strip("+")
    if st.count("+") < 15:
        mx = max(mx, len(st))
        continue
    st = st.split("+")
    for i in range(len(st) - 14):
        s = "+".join(st[i : i + 15])
        mx = max(mx, len(s))
print(mx)

# Solved by Аня


import re

s = open("1863_1.txt").readline()
m = re.findall(r"(?:[1-9][0-9]+[+]){14}[1-9][0-9]+", s)
print(len(max(m, key=len)))
print(max(m, key=len))

# Solved by Анастасия


import re

m = open("1863.txt").readline()
s = re.findall(r"(?:[1-9]+[+]){14}[1-9]+", m)
print(max(s, key=len))
print(len(max(s, key=len)))

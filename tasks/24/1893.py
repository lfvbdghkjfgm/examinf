# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\111\Downloads\24.txt").readline()

text = text.split("BC")

mx = 0

for i in range(len(text) - 190):
    s = "C" + "BC".join(text[i : i + 191]) + "B"
    mx = max(mx, len(s))

print(mx)

# Solved by Анастасия


s = open("1893.txt").readline()
s = s.split("BC")
m = []
for x in range(len(s) - 190):
    k = 0
    for y in range(191):
        k += len(s[x + y])
    m.append(k)
print(max(m) + 2 * 190)
# ненавижу цифру 2))) удалите её из мира пжпжпжпж

# Solved by София


s = open("24-11.txt").readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l : r + 1]
        if c.count("BC") > 190:
            break
        elif c.count("BC") == 190:
            m = max(m, len(c))
print(m)

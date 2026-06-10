# Solved by lfvbdghkjfgm
# https://lfvb.ru

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

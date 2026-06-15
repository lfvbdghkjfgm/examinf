# Solved by София


import re

s = open("1").readlines()
d = []
for x in s:
    if re.findall(r"195\.2[0-9]*[0-9]*\.[0-9][0-9]*[0-9]*\.14", x):
        d.append(x)
print(len(set(d)))

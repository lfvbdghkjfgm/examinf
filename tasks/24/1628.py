# Solved by lfvbdghkjfgm
# https://lfvb.ru
# More solves: https://github.com/lfvbdghkjfgm/examinf

import re

text = open(r"C:\Users\aatop\Downloads\1628_1.txt")
mx = 0

for x in text:
    if x.count("A") < 25:
        last_idx = {}
        for i in range(len(x)):
            if x[i] not in last_idx.keys():
                last_idx[x[i]] = [i]
            else:
                mx = max(i - last_idx[x[i]][0], mx)
                last_idx[x[i]].append(i)

print(mx)

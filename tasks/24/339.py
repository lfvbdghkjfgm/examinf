# Solved by Влад


from re import *

f = open("test.txt")
s = f.readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l : r + 1]
        if c.count("F") > 1:
            break
        if c.count("F") <= 1:
            m = max(len(c), m)
print(m)

# Solved by Влад


from re import *

f = open("test.txt")
s = f.readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l : r + 1]
        if c.count("AXMM") > 0:
            break
        if c.count("AXMM") == 0:
            m = max(len(c), m)
print(m)

# Solved by София


s = open("1").readline()
m = 0
c = ""
for r in range(len(s)):
    c += s[r]
    while "AXMM" in c:
        c = c[1:]
    m = max(len(c), m)
print(m)

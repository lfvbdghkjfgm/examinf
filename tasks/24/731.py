# Solved by Владимир Д.


import re

s = open("/home/student/Загрузки/731_1.txt").readline()

print(len(max(re.findall(r"[C-Z]+A[C-Z]+B[C-Z]+", s), key=len)))

# Solved by Влад


f = open("test.txt")
s = f.readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l : r + 1]
        if c.count("A") > 1:
            break
        if c.count("B") > 1:
            break
        if c.count("A") == 1 and c.count("B") == 1:
            m = max(m, len(c))
print(m)

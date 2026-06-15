# Solved by Влад


f = open("test.txt")
s = f.readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        c = s[l : r + 1]
        if c.count("X") > 1:
            break
        if c.count("Y") > 1:
            break
        if c.count("X") == 1 and c.count("Y") == 1:
            m = max(m, len(c))
print(m)

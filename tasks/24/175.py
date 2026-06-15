# Solved by Влад


f = open("test.txt")
s = f.readline()
m = 0
for l in range(len(s)):
    for r in range(l + m, len(s)):
        fl = 1
        c = s[l : r + 1]
        if c[0] != "O":
            break
        res = c.split("O")
        for i in range(len(res)):
            if res[i].count("F") > 2:
                fl = 0
        if fl == 0:
            break
        if c[0] == "O" and c[-1] == "O" and fl == 1:
            m = max(len(c), m)
print(m)
